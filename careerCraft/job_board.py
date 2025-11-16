def get_jobs(user_score, interests):
    jobs = [
        {"title": "Junior Python Developer", "company": "TechNova", "location": "Remote", "domain": "Tech"},
        {"title": "Digital Marketing Intern", "company": "Brandify", "location": "Mumbai", "domain": "Marketing"},
        {"title": "Graphic Designer", "company": "Creatix", "location": "Delhi", "domain": "Design"}
    ]
    return [job for job in jobs if job["domain"] in interests]
