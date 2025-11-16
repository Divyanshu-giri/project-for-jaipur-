def calculate_progress(actions):
    xp = 0
    badges = []
    if actions.get("quiz_completed"):
        xp += 50
        badges.append("Explorer")
    if actions.get("resume_generated"):
        xp += 100
        badges.append("Resume Ready")
    if actions.get("mentor_connected"):
        xp += 75
        badges.append("Networker")
    level = "Beginner"
    if xp >= 200:
        level = "Intermediate"
    if xp >= 400:
        level = "Pro"
    return {"xp": xp, "badges": badges, "level": level}
