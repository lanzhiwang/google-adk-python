from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm


# Define a tool function
def get_capital_city(country: str) -> str:
    """Retrieves the capital city for a given country."""
    # Replace with actual logic (e.g., API call, database lookup)
    capitals = {"france": "Paris", "japan": "Tokyo", "canada": "Ottawa"}
    return capitals.get(
        country.lower(), f"Sorry, I don't know the capital of {country}."
    )


# Add the tool to the agent
root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen3:32b"),
    name="capital_agent",
    description="Answers user questions about the capital city of a given country.",
    instruction="""You are an agent that provides the capital city of a country... (previous instruction text)""",
    tools=[get_capital_city],  # Provide the function directly
)
