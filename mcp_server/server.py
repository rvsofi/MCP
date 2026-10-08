from mcp.server import MCPServer

mcp = MCPServer("Week2 Multi Tool Server")


# Tool 1: Calculator
@mcp.tool()
def calculator(a: float, b: float, operation: str) -> float:
    """Perform basic arithmetic calculations."""

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    else:
        raise ValueError(
            "Invalid operation. Use add, subtract, multiply, or divide."
        )


# Tool 2: Word Counter
@mcp.tool()
def word_counter(text: str) -> int:
    """Count the number of words in a text."""
    return len(text.split())


# Sample employee data
employees = [
    {
        "id": 1,
        "name": "Arun Kumar",
        "department": "IT",
        "role": "Software Developer"
    },
    {
        "id": 2,
        "name": "Priya Sharma",
        "department": "HR",
        "role": "HR Executive"
    },
    {
        "id": 3,
        "name": "Rahul Raj",
        "department": "Finance",
        "role": "Accountant"
    },
    {
        "id": 4,
        "name": "Meena Devi",
        "department": "IT",
        "role": "System Engineer"
    }
]


# Tool 3: Employee Search
@mcp.tool()
def employee_search(name: str) -> list:
    """Search for an employee by name."""
    
    results = []

    for employee in employees:
        if name.lower() in employee["name"].lower():
            results.append(employee)

    return results


# Start MCP Server
if __name__ == "__main__":
    mcp.run()
    