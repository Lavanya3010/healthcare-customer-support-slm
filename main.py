from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from healthcare_rag import generate_answer

app = FastAPI(title="Healthcare SLM API")


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Healthcare SLM API is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        answer = generate_answer(request.question)

        if not answer:
            raise HTTPException(
                status_code=404,
                detail="No matching FAQ found"
            )

        return {"question": request.question, "answer": answer}

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))