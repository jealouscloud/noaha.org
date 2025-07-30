"""
SQLite database adapter

This module provides a connector for SQLite databases,
basic context management for sessions, and execution of SQL statements.

It also enables foregin key constraints and uses WAL mode.
"""

from pathlib import Path
from typing import Any, Literal, Mapping, Optional

import sqlalchemy
from sqlalchemy import (
    CursorResult,
    Executable,
    text,
)
from sqlalchemy.engine import Connection
from sqlalchemy.engine.interfaces import (
    CoreExecuteOptionsParameter,
    _CoreAnyExecuteParams,
)

CONNECTORS = {}

DEFAULT_KWARGS = {"pool_size": 100}


def _resolve_path(title) -> Path:
    data = Path("./data")
    if not data.exists():
        data.mkdir()

    return data / f"{title}.db"


class SqliteConnector:
    """
    A connection to a SQLite database.
    """

    ENGINES = {}

    def __init__(
        self,
        path,
        mode: Literal["ro", "rw", "rwc"] = "rw",
        timeout=5,
        **engine_kwargs: Optional[Mapping],
    ):
        self.path = _resolve_path(path)

        # hold the open conn if we have one
        self.conn: Optional[Connection] = None
        if mode == "rw":
            mode = "rwc"

        self.mode = mode
        self.timeout = timeout
        if engine_kwargs is None:
            engine_kwargs = {}

        _engine_kwargs = DEFAULT_KWARGS.copy() | engine_kwargs

        uri = f"{self.path}:{self.mode}"
        if uri in CONNECTORS:
            engine = CONNECTORS[uri]
        else:
            engine = sqlalchemy.create_engine(
                f"sqlite:///{self.connect_string()}",
                **_engine_kwargs,
            )
            CONNECTORS[uri] = engine
        self.engine = engine

    @property
    def connection(self) -> Connection:
        """
        Get the connection to the SQLite database.
        """
        if self.conn is None:
            raise RuntimeError("Database connection not established")
        return self.conn

    def execute(
        self,
        statement: Executable,
        parameters: Optional[_CoreAnyExecuteParams] = None,
        execution_options: Optional[CoreExecuteOptionsParameter] = None,
        *args,
        **kwargs,
    ) -> CursorResult[Any]:
        """
        Execute a SQL statement.  
        :param statement: The SQL statement to execute.  
        :param parameters: Optional parameters for the SQL statement.  
        :param execution_options: Optional execution options for the SQL statement.  
        :return: The result of the SQL statement execution.  
        """  # fmt: skip
        return self.connection.execute(
            statement,
            parameters=parameters,
            execution_options=execution_options,
            *args,
            **kwargs,
        )

    def connect_string(self) -> str:
        return f"{self.path}?mode={self.mode}&timeout={self.timeout}"

    def __enter__(self):
        """Establish a connection to the SQLite database and start transaction"""
        if self.conn:
            raise RuntimeError(
                "Database connection already established, use __exit__ to close it"
            )

        conn = self.engine.connect()
        self.conn = self.engine.connect()
        # conn.__enter__()  # start transaction
        # WAL generally more efficient for concurrent reads/writes
        conn.execute(text("PRAGMA journal_mode=WAL"))
        # Enable foreign key constraints
        conn.execute(text("PRAGMA foreign_keys=ON"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is None and exc_val is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.__exit__(exc_type, exc_val, exc_tb)
            self.conn.close()
            self.conn = None
