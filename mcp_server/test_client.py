import asyncio
import sys

from mcp import Client
from mcp import StdioServerParameters


async def main():
    server = StdioServerParameters(
        command=sys.executable,
        args=["server.py"]
    )

    async with Client(server) as client:

        # Show available tools
        tools = await client.list_tools()

        print("\nAvailable MCP Tools:")
        for tool in tools.tools:
            print("-", tool.name)

        # Test Calculator
        calculator_result = await client.call_tool(
            "calculator",
            {
                "a": 10,
                "b": 5,
                "operation": "add"
            }
        )

        print("\nCalculator Test:")
        print(calculator_result)

        # Test Word Counter
        word_result = await client.call_tool(
            "word_counter",
            {
                "text": "Model Context Protocol"
            }
        )

        print("\nWord Counter Test:")
        print(word_result)

        # Test Employee Search
        employee_result = await client.call_tool(
            "employee_search",
            {
                "name": "Arun"
            }
        )

        print("\nEmployee Search Test:")
        print(employee_result)


if __name__ == "__main__":
    asyncio.run(main())