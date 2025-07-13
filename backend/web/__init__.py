def main() -> int:
    """
    Entry point for the web application.

    This function is used to start the web server.
    """
    from .wsgi import run

    run()
    return 0
