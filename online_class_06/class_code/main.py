from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP(stateless_http=True, name="Hello prompt")

@mcp.prompt()
async def hello_prompt() -> list[base.UserMessage]:
    user_message = f"Hello, From Agentic Mars!"
    return {base.UserMessage(content=user_message)} , {base.AssistantMessage(content="Hi there! How can I assist you today?")}

mcp_app = mcp.streamable_http_app() 