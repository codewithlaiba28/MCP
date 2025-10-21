from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="MCP Client", stateless_http=True)

docs = {
    "intro": "This is an example MCP server.",
    "readme": "Welcome to the MCP server! This server provides various tools and resources.",
    "guide": "To use this MCP server, connect using an MCP client and explore the available tools and resources.",
}

@mcp.resource("docs://documents", 
              mime_type="application/json")
def list_docs():
    """list available document names"""
    return list(docs.keys())

print(f"list_docs: {list_docs()}")

mcp_server = mcp.streamable_http_app()