"""
live-reload.py

This script starts your server application in debug mode
with live-reloading capabilities.

Reloads will also trigger the browser to update with detected changes.

Additional reload conditions are specified with optional trigger commands
i.e if you have to compile css or js for your frontend.

In this project, this is best run via `rye run dev`
"""

import shutil

import html_compose.live as live

assert shutil.which("rye"), "rye not found, please install it."
assert shutil.which("pnpm"), "pnpm not found, please install it."


live.server(
    daemon=live.ShellCommand(
        "rye run flask --app  ./backend/web/server.py run"
    ),
    daemon_delay=0.2,
    conds=[
        live.WatchCond(
            path_glob="backend/**/*.py", action=live.ShellCommand("date")
        ),
        live.WatchCond(path_glob="content/*.md", action=None),
        live.WatchCond(
            ["frontend/**/*.js", "frontend/**/*.css"],
            action=live.ShellCommand("cd frontend && pnpm build"),
            ignore_glob=["frontend/node_modules/"],
            reload=False,
        ),
        live.WatchCond(
            "public/**/*",
            action=None,
            server_reload=False,
        ),
    ],
    host="localhost",
    port=51353,
    livereload_delay=0.5,
)
