from abc import ABC, abstractmethod
from mcp.server.fastmcp import FastMCP

class BaseTool(ABC):
    def __init__(self, mcp: FastMCP):
        self.mcp = mcp
        self.register_tools()
    
    @abstractmethod
    def register_tools(self):
        """Método abstracto que cada herramienta debe implementar"""
        pass