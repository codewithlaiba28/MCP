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

@mcp.resource("docs://documents/{doc_name}", 
              mime_type="text/plain")

def read_docs(doc_name:str):
    """Read a specific document."""
    if doc_name in docs:
        return docs[doc_name]
    else:
        raise mcp.ResourceNotFound(f"Document '{doc_name}' not found.")

# def read_docs(doc_name:str):
#     """read document by name"""
#     return docs.get(doc_name, "Document not found.")

# print(f"list_docs: {list_docs()}")

mcp_server = mcp.streamable_http_app()