
from app.services.ollama_service import query_ollama

def get_research_content(topic):
    prompt = f"Provide detailed research on '{topic}' from three perspectives: web content (overview and examples), video lecture transcript summary, and academic insights with references."
    llm_response = query_ollama(prompt)
    return {
        "web": f"Web summary for {topic}: {llm_response}",
        "video": f"Video-style explanation: {llm_response}",
        "academic": f"Academic-style explanation with references: {llm_response}"
    }
