from mcp.server.fastmcp import FastMCP

app = FastMCP(stateless_http=False, json_response=False)

mcp_app = app.streamable_http_app()


from mcp.server.fastmcp import FastMCP

app = FastMCP(stateless_http=True)

mcp_app = app.streamable_http_app()