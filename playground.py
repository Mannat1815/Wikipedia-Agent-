import os
from dotenv import load_dotenv
import openai

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.wikipedia import WikipediaTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app

# Load environment variables from .env file
load_dotenv()

# Set PHI API Key via environment variables.getenv("phi-uD48Zsl6deRrZR1PioFH3lH8yj
os.environ["PHI_API_KEY"] = os.getenv("PHI_API_KEY")  # Your .env should include this key

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama3-70b-8192"),  # Groq's valid model ID
    tools=[DuckDuckGo()],
    instructions=["Always include sources."],
    show_tools_calls=True,
    markdown=True,
)

# Wikipedia Agent
wikipedia_agent = Agent(
    name="Wikipedia AI Agent",
    role="Fetch and summarize information from Wikipedia",
    model=Groq(id="llama3-70b-8192"),
    tools=[WikipediaTools()],
    instructions=["Use tables to display structured data if applicable."],
    show_tools_calls=True,
    markdown=True,
)

# Create the Playground app
app = Playground(agents=[wikipedia_agent, web_search_agent]).get_app()

# Serve the app
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
