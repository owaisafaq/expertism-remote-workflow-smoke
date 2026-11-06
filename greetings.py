def greet(name: str) -> str:
    """Return a greeting, using World when no name is supplied."""
    return f"Hello, {name or 'World'}!"
