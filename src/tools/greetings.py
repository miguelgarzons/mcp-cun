from mcp.server.fastmcp import tool

@tool()
def say_hello(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"
