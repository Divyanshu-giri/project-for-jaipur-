def generate_questions(career):
    return {
        "Software Developer": ["Tell me about a project where you used Python."],
        "Digital Marketer": ["How would you grow a brand on Instagram?"]
    }.get(career, ["Tell me about yourself."])

def score_answer(answer):
    length = len(answer.split())
    confidence = "High" if length > 20 else "Medium" if length > 10 else "Low"
    relevance = "Good" if "project" in answer or "experience" in answer else "Needs Work"
    return {"confidence": confidence, "relevance": relevance}
