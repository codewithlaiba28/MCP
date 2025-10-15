from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="hello_mcp", stateless_http=True)

@mcp.tool()
def search_online(query: str) -> str:
    return f"Results for '{query}' from online search."

@mcp.tool()
async def get_weather(query: str) -> str:
    return f"Results for '{query}' from weather."

mcp_app = mcp.streamable_http_app()