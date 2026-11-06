def greet(name: str) -> str:
    """Return a greeting, using World when no name is supplied.

    Leading and trailing whitespace is trimmed; whitespace inside the name is kept.
    """
    trimmed = (name or "").strip()
    return f"Hello, {trimmed or 'World'}!"
