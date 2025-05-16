from pathlib import Path

cbcache = {}


def cache_bust(path):
    """
    This is a static resource helper function that returns
    given path + modification time of a file.

    It is for cachebusting.
    """
    global cbcache
    if path not in cbcache:
        p = Path(".").resolve()
        # pathlib will think we mean absolute if path starts with a slash
        p = p / path.lstrip("/")
        if p.exists():
            mtime = p.stat().st_mtime
            if len(cbcache) > 1000:  # clear cache if it's too big
                cbcache.clear()

            cbcache[path] = int(mtime)
        else:
            raise FileNotFoundError(
                f"No such file or directory ?: {p.absolute()}"
            )

    return f"{path}?vers={cbcache[path]}"
