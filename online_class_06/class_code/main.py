from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP(stateless_http=True, name="Hello prompt")

@mcp.prompt()
async def hello_prompt(name: str) -> str:
    return f"Hello, {name}!" 

mcp_app = mcp.streamable_http_app() 