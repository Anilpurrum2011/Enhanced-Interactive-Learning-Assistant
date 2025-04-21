
def ask_questions(request):
    return {
        "clarification": f"What specific aspect of '{request.topic}' are you most curious about?",
        "format": f"Do you prefer deep theoretical learning or quick practical insights in {request.preferred_format}?",
        "depth": f"Considering your prior knowledge is '{request.prior_knowledge}', should the learning material include beginner-level concepts?"
    }
