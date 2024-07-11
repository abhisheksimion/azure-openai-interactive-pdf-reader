import requests


# Tool functions
def lookup_url(query):
    try:
        response = requests.get(query)
        return response.text
    except Exception as e:
        return f"Error fetching URL: {e}"


def search_online(query):
    return f"Simulated search results for query: {query}"


# Tool registration and execution
class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name, func, description, parameters):
        self.tools[name] = {
            "func": func,
            "description": description,
            "parameters": parameters
        }

    def execute_tool(self, tool_name, parameters):
        if tool_name in self.tools:
            tool = self.tools[tool_name]
            func = tool['func']
            required_params = tool['parameters']

            # Validate parameters
            if set(parameters.keys()) == set(required_params.keys()):
                return func(**parameters)
            else:
                return f"Function {tool_name} called with incorrect arguments."
        else:
            return f"Function {tool_name} not found."


# Initialize the tool registry
tool_registry = ToolRegistry()

# Register tools
tool_registry.register_tool(
    name="lookup_url",
    func=lookup_url,
    description="This tool helps to get the latest details from a URL for the user",
    parameters={"query": str}
)

tool_registry.register_tool(
    name="search_online",
    func=search_online,
    description="This tool helps to get details from the internet for the user.",
    parameters={"query": str}
)
