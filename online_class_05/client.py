import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
from contextlib import AsyncExitStack
from mcp import types
from typing import Any
from pydantic import AnyUrl
 

class MCPClient:
    def __init__(self, url):
        self.url = url
        self.stack = AsyncExitStack()
        self._sess = None

    async def list_tools(self):
        async with self.session as session:
            response = (await session.list_tools()).tools
            return response
        
    async def __aenter__(self): 
       read, write, _ = await self.stack.enter_async_context(
            streamablehttp_client(self.url)
        )   
       self._sess = await self.stack.enter_async_context(
           ClientSession(read, write)
       )
       
       await self._sess.initialize()
       return self
       

    async def __aexit__(self, *args):
       await self.stack.aclose() 

    async def list_tools(self) -> list[types.Tool]:
        return (await self._sess.list_tools()).tools
    
    
    async def list_resources(self) -> list[types.Resource]:
        result:types.ListResourcesResult= await self._sess.list_resources()
        return result.resources
    
    async def read_resources(self, uri:str) ->types.Resource:
        result = await self._sess.read_resource(uri)
        return result.resource

async def main():
    async with MCPClient("http://localhost:8000/mcp") as client:
        tools = await client.list_tools()
        print(tools, "tools")

        resources = await client.list_resources()
        print(resources, "resources")


asyncio.run(main())

