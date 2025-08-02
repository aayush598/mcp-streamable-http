from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp.server.fastmcp import tools

async def run():
    async with sse_client(url="http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(tools)

            result = await session.call_tool("add", arguments={"a": 4, "b": 5})
            print(result.content[0].text)
            
            
if __name__ == "__main__":
    import asyncio
    asyncio.run(run())  