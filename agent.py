import os
from dotenv import load_dotenv


from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.wikipedia import WikipediaTools
from phi.tools.duckduckgo import DuckDuckGo

# Load environment variables from .env file
load_dotenv()

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

multi_agent = Agent(
    team=[web_search_agent, wikipedia_agent],
    instructions=[
    
        "Always include sources when providing information.",
        "Use tables to display the data.",
    ],
    show_tool_calls=True,
    markdown=True,
    model=Groq(id="llama-3.3-70b-versatile", api_key="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"),
)


multi_agent.print_response("what is the history of India",stream=True)
