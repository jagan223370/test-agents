from google.adk.agents import Agent
from google.adk.models.lite_llm import Litellm

#Set the Agent Model
AGENT_MODEL = "ollama/llama3.1"

#template
root_agent = Agent(
    name = "greet_agent",
    model = LiteLlm(model=AGENT_MODEL),
    description = "Acts like a Greeter",
    instruction = "You are a greeter who will greet a person who comesin with warm wishes for long life" 
)