from google.adk.agents.llm_agent import Agent
from google.adk.apps import App
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen3:32b"),
    name="greeter_agent",
    description="An agent that provides a friendly greeting.",
    instruction="Reply with Hello, World!",
)

app = App(
    name="agents",
    root_agent=root_agent,
    # Optionally include App-level features:
    # plugins, context_cache_config, resumability_config
)
