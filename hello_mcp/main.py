from mcp.server.fastmcp import FastMCP

mcp= FastMCP(name="mcp", stateless_http=True)

@mcp.tool(name="search_online", description="Search online for a query")
def online_search(query: str):
    return f"Hi, How are you . Your answer is {query}"

mcp_run = mcp.streamable_http_app()
