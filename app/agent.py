import os
import truststore
from dotenv import load_dotenv

# Inject Windows system certificate store (includes corporate/Nokia CA)
truststore.inject_into_ssl()

from google.adk.agents import Agent
from app.prompt import SYSTEM_PROMPT


load_dotenv()

root_agent = Agent(
    name="ai_learning_agent",
    model="gemini-2.5-flash",
    description="An AI learning assistant that summarizes, explains, and generates interview questions.",
    instruction=SYSTEM_PROMPT,
)