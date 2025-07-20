from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("fastmcp-starter-kit", port=8000)


@mcp.tool()
async def get_author_name() -> str:
    """Get the name of the author of this MCP server."""
    return "Sujjad Shaik"


if __name__ == "__main__":
    mcp.run(transport="sse")
