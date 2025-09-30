
import os
import uvicorn
from mcp.server.fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware

mcp = FastMCP(name="Say Hello")



def main():
    print("Say Hello MCP Server starting...")
    app = mcp.streamable_http_app()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
        expose_headers=["mcp-session-id", "mcp-protocol-version"],
        max_age=86400,
    )
    port = int(os.environ.get("PORT", 8080))
    print(f"Listening on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="debug")

if __name__ == "__main__":
    main()