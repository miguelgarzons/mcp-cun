# En tools/greetings.py - pasarle mcp como parámetro
def register_tools(mcp):
    @mcp.tool()
    def say_hello(name: str) -> str:
        """Greet a user by name."""
        return f"Hello, {name}!"