
from fastapi import FastAPI
from pydantic import BaseModel
from app.services import research_service, question_service, report_service

app = FastAPI()

class LearningRequest(BaseModel):
    topic: str
    objective: str
    prior_knowledge: str = "beginner"
    preferred_format: str = "text"

@app.post("/learn")
async def learn(request: LearningRequest):
    research = research_service.get_research_content(request.topic)
    questions = question_service.ask_questions(request)
    report = report_service.generate_report(request.topic, request.objective, research, questions)
    return {"report": report, "questions": questions}

@app.post("/update-report")
async def update_report(request: LearningRequest):
    return {"modified_report": f"Updated report based on feedback: {request.dict()}"}
