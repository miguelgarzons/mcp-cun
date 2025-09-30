from .base import BaseTool

class GreetingsTool(BaseTool):
    def register_tools(self):
        @self.mcp.tool()
        def say_hello(name: str) -> str:
            """Greet a user by name."""
            return f"Hello, {name}!"
        
        @self.mcp.tool()
        def say_goodbye(name: str) -> str:
            """Say goodbye to a user by name."""
            return f"Goodbye, {name}!"