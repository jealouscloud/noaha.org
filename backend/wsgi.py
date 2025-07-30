"""
Production script to gunicorn wsgi server.
"""

import os

from gunicorn.app.base import BaseApplication
from loguru import logger

from .server import app


class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        if not self.cfg:
            logger.error("Gunicorn configuration is not set.")
            return

        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }

        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def run():
    host = os.environ.get("HOST", "0.0.0.0")
    port = os.environ.get("PORT", "8000")
    workers = os.environ.get("WORKERS", "4")
    options = {
        "bind": f"{host}:{port}",
        "workers": workers,
    }
    StandaloneApplication(app, options).run()
