from fastapi import FastAPI
from pydantic import BaseModel
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from app.agent import root_agent

app = FastAPI()

VALID_MODES = ["summarize", "explain", "interview"]

session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
    app_name="ai_learning_agent",
    session_service=session_service,
)


class RequestBody(BaseModel):
    input_text: str
    mode: str


@app.get("/")
def home():
    return {"message": "AI Learning Agent is running 🚀"}


@app.post("/learn")
async def learn(req: RequestBody):
    mode = req.mode if req.mode else "explain"

    if mode not in VALID_MODES:
        return {"error": "Invalid mode. Use summarize/explain/interview"}

    session = await session_service.create_session(
        app_name="ai_learning_agent",
        user_id="user",
    )

    message = Content(
        role="user",
        parts=[Part(text=f"Mode: {mode}\n\n{req.input_text}")],
    )