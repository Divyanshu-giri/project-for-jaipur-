def match_mentors(user_score, interests):
    mentors = [
        {"name": "Aditi Sharma", "field": "AI & ML", "score_range": (12, 15)},
        {"name": "Ravi Mehta", "field": "Web Dev", "score_range": (8, 12)},
        {"name": "Neha Verma", "field": "Marketing", "score_range": (5, 10)}
    ]
    return [m for m in mentors if user_score >= m["score_range"][0] and user_score <= m["score_range"][1]]
