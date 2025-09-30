from .base import BaseTool

class CalculatorTool(BaseTool):
    def register_tools(self):
        @self.mcp.tool()
        def add(a: int, b: int) -> int:
            """Add two numbers."""
            return a + b
        
        @self.mcp.tool()
        def multiply(a: int, b: int) -> int:
            """Multiply two numbers."""
            return a * b