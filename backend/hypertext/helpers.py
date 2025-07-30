from pathlib import Path

cachebust_cache = {}


def cache_bust(path):
    """
    This is a static resource helper function that returns
    given path + modification time of a file.

    It is for cachebusting.
    """
    global cachebust_cache
    if path not in cachebust_cache:
        p = Path(".").resolve()
        # pathlib will think we mean absolute if path starts with a slash
        p = p / path.lstrip("/")
        if p.exists():
            mtime = p.stat().st_mtime
            if len(cachebust_cache) > 10000:  # clear cache if it's too big
                cachebust_cache.clear()

            cachebust_cache[path] = int(mtime)
        else:
            raise FileNotFoundError(
                f"No such file or directory ?: {p.absolute()}"
            )

    return f"{path}?vers={cachebust_cache[path]}"
