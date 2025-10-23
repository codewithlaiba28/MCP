import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
from contextlib import AsyncExitStack
from mcp import types
from typing import Any
import json 
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
        assert self._sess, "session not available"

        return (await self._sess.list_tools()).tools
    
    
    async def list_resources(self) -> list[types.Resource]:
        assert self._sess, "session not available"

        result:types.ListResourcesResult= await self._sess.list_resources()
        return result.resources
    

    async def list_resources_Template(self) ->list[types.Resource]:
        assert self._sess, "session not available"
        result: types.ListResourcesResult= await self._sess.list_resource_templates()
        # print(f"LIST RESOURCES TEMPLATE DICT{result.__dict__}")
        return result.resourceTemplates

    async def read_resources(self, uri:str) ->types.ReadResourceResult:
        assert self._sess, "session not available"
        _url = AnyUrl(uri)
        result = await self._sess.read_resource(_url)
        # print(f"READ RESOURCES DICT{result.__dict__}")
        resource = result.contents[0]
        if isinstance(resource, types.TextResourceContents):
            if resource.mimeType == "application/json":
                try:
                    return json.loads(resource.text)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
            # return resource
        return resource.text

async def main():
    async with MCPClient("http://localhost:8000/mcp") as client:
        # tools = await client.list_tools()
        # print(tools, "tools")

        # resources = await client.list_resources()
        # data= await client.read_resources("docs://documents")

        # print(resources[0].uri, "first resource uri")
        # print(data, "data from first resource")
         
        # for r in resources:
        #     data= await client.read_resources(r.uri)
        #     print(f"Data for {r.uri}: ___________________{data}")

        # template = await client.list_resources_Template()
        # print(template, "template resources")
        # for i in template:
        #    print("__________________________________________________________________________")
        #    print(f"Template Resource: {i.uriTemplate}") 
        #    data = await client.read_resources(i.uriTemplate)
        #    print("__________________________________________________________________________")
        template = await client.list_resources_Template()
        intro_uri = template[0].uriTemplate.replace("{doc_name}", "intro")
        data = await client.read_resources(intro_uri)
        print("Indtro Document Data:",data)
        # print(f"Resources Template: {template[0].uriTemplate}")
        # template = await client.list_resources_Template()
        # print("Resource Templates:", template[0].uriTemplate)
asyncio.run(main())

