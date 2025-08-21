from flask import Flask, render_template, request, redirect, url_for, flash, session
from resume_builder import generate_resume
from mentor_matcher import match_mentors
from progress_tracker import calculate_progress
from interview_simulator import generate_questions, score_answer
from job_board import get_jobs
import re

app = Flask(__name__)
app.secret_key = 'career-craft-secret'  # Needed for flash messages




# Section routes (must be after app is defined)
@app.route('/mentors')
def mentors():
    # Demo: use default data
    score = 13
    field = 'Software Developer'
    mentors = match_mentors(score, [field])
    return render_template('mentors.html', mentors=mentors)

@app.route('/jobs')
def jobs():
    score = 13
    field = 'Software Developer'
    jobs = get_jobs(score, [field])
    return render_template('jobs.html', jobs=jobs)

@app.route('/progress')
def progress():
    progress = calculate_progress({
        "quiz_completed": True,
        "resume_generated": True,
        "mentor_connected": True
    })
    return render_template('progress.html', progress=progress)


@app.route('/roadmap')
def roadmap():
    roadmap = get_roadmap_for_field('Software Developer')
    return render_template('roadmap.html', roadmap=roadmap)




@app.route('/')
def login():
    return render_template('login.html')

# Step 1: After login, show career selection and survey
@app.route('/survey', methods=['POST', 'GET'])
def survey():
    if request.method == 'POST':
        # Save user info from login
        name = request.form.get('name', 'Student')
        email = request.form.get('email', '')
        number = request.form.get('number', '')
        password = request.form.get('password', '')
        # Validate mobile number: must be 10 digits
        if not re.fullmatch(r"\d{10}", number):
            flash('Mobile number must be exactly 10 digits.')
            return redirect(url_for('login'))
        if not name.strip():
            flash('Name is required.')
            return redirect(url_for('login'))
        if not password or len(password) < 6:
            flash('Password must be at least 6 characters.')
            return redirect(url_for('login'))
        # Pass user info to survey page
        return render_template('survey.html', name=name, email=email, number=number)
    else:
        return redirect(url_for('login'))

# Step 2: Handle survey submission and show dashboard
@app.route('/dashboard', methods=['POST'])
def dashboard():
    name = request.form.get('name', 'Student')
    email = request.form.get('email', '')
    number = request.form.get('number', '')
    career = request.form.get('career', 'Software Developer')
    hobbies = request.form.get('hobbies', '')
    field = request.form.get('field', career)
    # Simulate score and interests
    score = 13
    user_data = {"name": name, "email": email, "score": score, "career": career, "hobbies": hobbies, "field": field}
    resume = generate_resume(user_data)
    mentors = match_mentors(score, [field])
    progress = calculate_progress({
        "quiz_completed": True,
        "resume_generated": True,
        "mentor_connected": True
    })
    jobs = get_jobs(score, [field])
    questions = generate_questions(career)
    # For demo: add YouTube links and job ready checklist
    courses = get_courses_for_field(field)
    roadmap = get_roadmap_for_field(field)
    return render_template("dashboard.html", resume=resume, mentors=mentors, progress=progress, jobs=jobs, questions=questions, courses=courses, roadmap=roadmap, field=field)

# Helper: Dummy course and roadmap data
def get_courses_for_field(field):
    # In real app, fetch from DB or API
    yt = {
        "Software Developer": [
            {"title": "Python Crash Course", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"},
            {"title": "Web Dev for Beginners", "url": "https://www.youtube.com/watch?v=Q33KBiDriJY"}
        ],
        "Data Scientist": [
            {"title": "Data Science Roadmap", "url": "https://www.youtube.com/watch?v=ua-CiDNNj30"}
        ],
        "Digital Marketer": [
            {"title": "Digital Marketing Basics", "url": "https://www.youtube.com/watch?v=nJkVHusJIQk"}
        ]
    }
    return yt.get(field, [])

def get_roadmap_for_field(field):
    maps = {
        "Software Developer": ["Learn Python", "Build Projects", "Master Data Structures", "Apply for Internships"],
        "Data Scientist": ["Learn Python & Statistics", "Practice ML", "Build Data Projects", "Apply for Data Roles"],
        "Digital Marketer": ["Learn SEO", "Content Creation", "Analytics Tools", "Apply for Marketing Jobs"]
    }
    return maps.get(field, [])

@app.route('/resume')
def resume():
    user = session.get('user', {"name": "Student", "email": "student@example.com"})
    resume = generate_resume({"name": user.get('name', 'Student'), "email": user.get('email', ''), "score": 13})
    return render_template('resume.html', resume=resume)

@app.route('/interview', methods=['POST'])
def interview():
    answer = request.form['answer']
    feedback = score_answer(answer)
    return render_template('interview_feedback.html', feedback=feedback)


# Google Meet page
@app.route('/meet')
def meet():
    # In a real app, user_id could be from session or login
    user_id = '12345'
    return render_template('meet.html', user_id=user_id)

# AI Mentor & Assistant page
@app.route('/assistant')
def assistant():
    return render_template('assistant.html')


# Courses page
@app.route('/courses')
def courses():
    # For demo, show all Software Developer courses if no user context
    courses = get_courses_for_field('Software Developer')
    return render_template('courses.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)
