from mcp.server.fastmcp import FastMCP

# stateless_http=False by default
# Here we explicitly set it to False for clarity
mcp = FastMCP("weather", stateless_http=False)

@mcp.tool()
async def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    # In a real implementation, this function would call a weather API.
    return f"The current weather in {city} is sunny with a temperature of 25°C."


mcp_app = mcp.streamable_http_app()