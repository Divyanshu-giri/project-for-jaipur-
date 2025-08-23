def generate_resume(data):
    name = data.get('name', 'Student')
    email = data.get('email', '')
    score = data.get('score', 0)
    photo = data.get('photo', 'https://randomuser.me/api/portraits/men/1.jpg')
    about = data.get('about', 'Passionate learner ready to grow!')
    education = data.get('education', 'Not specified')
    hobbies = data.get('hobbies', '')
    skills = data.get('skills', [])
    # Default skills if not provided
    if not skills:
        if score >= 12:
            skills = ["Python", "Problem Solving", "Web Development"]
        elif score >= 8:
            skills = ["SEO", "Content Creation", "Analytics"]
        else:
            skills = ["Communication", "Empathy", "CRM Tools"]
    career = data.get('career', 'Software Developer' if score >= 12 else 'Digital Marketer' if score >= 8 else 'Customer Support Executive')
    return {
        "name": name,
        "email": email,
        "career": career,
        "skills": skills,
        "summary": data.get('summary', f"Aspiring {career} with strong foundational skills."),
        "photo": photo,
        "about": about,
        "education": education,
        "hobbies": hobbies
    }
