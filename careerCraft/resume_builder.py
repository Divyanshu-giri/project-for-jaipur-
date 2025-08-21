def generate_resume(data):
    name = data.get('name', 'Student')
    email = data.get('email', '')
    score = data.get('score', 0)
    if score >= 12:
        career = "Software Developer"
        skills = ["Python", "Problem Solving", "Web Development"]
    elif score >= 8:
        career = "Digital Marketer"
        skills = ["SEO", "Content Creation", "Analytics"]
    else:
        career = "Customer Support Executive"
        skills = ["Communication", "Empathy", "CRM Tools"]
    return {
        "name": name,
        "email": email,
        "career": career,
        "skills": skills,
        "summary": f"Aspiring {career} with strong foundational skills."
    }
