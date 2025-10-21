from mcp.server.fastmcp import FastMCP


mcp_app = FastMCP(name="MCP Client", stateless_http=True)


mcp_server = mcp_app.streamable_http_app()

# with open("data.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)
    

    
# with open("data.txt", "w") as file:
#     file.write("This is new line\n")


# with open("data.txt", "r+") as file, open("out.txt", "w") as outfile:
#     lines = file.read()
#     outfile.write(lines)
#     print(lines)
    
# import asyncio
# from contextlib import asynccontextmanager

# @asynccontextmanager
# async def make_connection(name):
#     print(f"Making connection... {name}")
#     yield name
#     print(f"Connection established. {name}")
    

# async def main():
#     async with make_connection("A") as a:
#         print(f"Using connection: {a}")
#     print("Connection closed.") 


# asyncio.run(main())           




# import asyncio

# async def get_connection(name):
#     class ctx:
#         async def __aenter__(self):
#             print(f"Making connection... {name}")
#             return name

#         async def __aexit__(self, exc_type, exc, tb):
#             print(f"Connection established. {name}")

#     return ctx()   


# async def main():
#     async with await get_connection("A") as a:
#         async with await get_connection("B") as b:
#             print(f"Using connection: {a} and {b}")
#     print("Connection closed.")

# asyncio.run(main())   












# import asyncio
# from contextlib import AsyncExitStack

# async def get_connection(name):
#     class ctx:
#         async def __aenter__(self):
#             print(f"Enter {name}")
#             return name

#         async def __aexit__(self, exc_type, exc, tb):
#             print(f"Exit {name}")

#     return ctx()   


# async def main():
#     async with AsyncExitStack() as stack:
#         a = await stack.enter_async_context(await get_connection("A"))
#         b = await stack.enter_async_context(await get_connection("B"))
#         print(f"Using connection: {a} and {b}")

#         async def custom_cleanup():
#             print("Custom cleanup actions here.")

#         stack.push_async_callback(custom_cleanup)
#         print(f"Doing work with connection: {a} and {b} and may be {locals().get('b')} ")

#         await asyncio.sleep(1)
#     print("Connection closed.")
# asyncio.run(main())  