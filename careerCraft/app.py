import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Mentor, Job, Course, RoadmapStep, UserProgress, MentorConnection
from resume_builder import generate_resume
from mentor_matcher import match_mentors
from progress_tracker import calculate_progress
from interview_simulator import generate_questions, score_answer
from job_board import get_jobs
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'career-craft-secret'

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'careercraft.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Directory for uploaded profile images
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'profile_photos')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




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


@app.route('/roadmap', methods=['GET', 'POST'])
def roadmap():
    # Get the selected field from the request or use the user's field from session
    selected_field = request.args.get('field')
    if not selected_field and 'user_data' in session:
        selected_field = session['user_data'].get('field', 'Software Developer')
    elif not selected_field:
        selected_field = 'Software Developer'
    
    # Get roadmap for the selected field
    roadmap = get_roadmap_for_field(selected_field)
    
    # Get available fields for dropdown
    available_fields = get_available_fields()
    
    return render_template('roadmap.html', roadmap=roadmap, selected_field=selected_field, available_fields=available_fields)

def get_available_fields():
    """Return list of available career fields"""
    return ["Software Developer", "Data Scientist", "Digital Marketer", "Web Developer", "AI Engineer", "UX Designer"]




@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Example: check credentials (add your own logic)
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:  # Replace with real authentication
            session['user'] = email
            return redirect(url_for('survey'))
        else:
            # Optionally flash an error message
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # Save survey data to session
        name = request.form.get('name', 'Student')
        email = request.form.get('email', '')
        number = request.form.get('number', '')
        career = request.form.get('career', 'Software Developer')
        hobbies = request.form.get('hobbies', '')
        field = request.form.get('field', career)
        
        # Store user data in session
        session['user_data'] = {
            'name': name,
            'email': email,
            'number': number,
            'career': career,
            'hobbies': hobbies,
            'field': field,
            'score': 13  # Default score for demo
        }
        
        return redirect(url_for('dashboard'))
    return render_template('survey_enhanced.html')

# Step 2: Handle survey submission and show dashboard
@app.route('/dashboard', methods=['POST'])
def dashboard_post():
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
    return render_template("dashboard_enhanced.html", resume=resume, mentors=mentors, progress=progress, jobs=jobs, questions=questions, courses=courses, roadmap=roadmap, field=field)

# GET route for dashboard navigation
@app.route('/dashboard', methods=['GET'])
def dashboard():
    # For GET requests, show a basic dashboard or redirect to survey if no data
    # You can store user data in session and retrieve it here
    if 'user_data' in session:
        user_data = session['user_data']
        resume = generate_resume(user_data)
        mentors = match_mentors(user_data.get('score', 13), [user_data.get('field', 'Software Developer')])
        progress = calculate_progress({
            "quiz_completed": True,
            "resume_generated": True,
            "mentor_connected": True
        })
        jobs = get_jobs(user_data.get('score', 13), [user_data.get('field', 'Software Developer')])
        questions = generate_questions(user_data.get('career', 'Software Developer'))
        courses = get_courses_for_field(user_data.get('field', 'Software Developer'))
        roadmap = get_roadmap_for_field(user_data.get('field', 'Software Developer'))
        return render_template("dashboard_enhanced.html", resume=resume, mentors=mentors, progress=progress, jobs=jobs, questions=questions, courses=courses, roadmap=roadmap, field=user_data.get('field', 'Software Developer'))
    else:
        # If no user data, redirect to survey
        return redirect(url_for('survey'))

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
        ],
        "Web Developer": [
            {"title": "HTML & CSS Tutorial", "url": "https://www.youtube.com/watch?v=qz0aGYrrlhU"},
            {"title": "JavaScript Mastery", "url": "https://www.youtube.com/watch?v=hdI2bqOjy3c"}
        ],
        "AI Engineer": [
            {"title": "Machine Learning Fundamentals", "url": "https://www.youtube.com/watch?v=aircAruvnKk"},
            {"title": "Deep Learning Specialization", "url": "https://www.youtube.com/watch?v=CS4cs9xVecg"}
        ],
        "UX Designer": [
            {"title": "UX Design Principles", "url": "https://www.youtube.com/watch?v=Ovj4hFxko7c"},
            {"title": "Figma Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=FTFaQWZBqQ8"}
        ]
    }
    return yt.get(field, [])

def get_roadmap_for_field(field):
    maps = {
        "Software Developer": ["Learn Python", "Build Projects", "Master Data Structures", "Apply for Internships"],
        "Data Scientist": ["Learn Python & Statistics", "Practice ML", "Build Data Projects", "Apply for Data Roles"],
        "Digital Marketer": ["Learn SEO", "Content Creation", "Analytics Tools", "Apply for Marketing Jobs"],
        "Web Developer": ["Learn HTML/CSS", "Master JavaScript", "Study Frameworks (React/Vue)", "Build Portfolio Projects"],
        "AI Engineer": ["Learn Python & Math", "Study Machine Learning", "Deep Learning Concepts", "Build AI Projects"],
        "UX Designer": ["Learn Design Principles", "Study User Research", "Master Design Tools", "Build Design Portfolio"]
    }
    return maps.get(field, [])

from flask import jsonify

# Profile view and edit
@app.route('/resume')
def resume():
    if 'user_data' in session:
        # Use the user data from session
        resume_data = session['user_data'].copy()
        # Ensure all required fields are present
        resume_data.setdefault('name', 'Student')
        resume_data.setdefault('email', session.get('user', ''))
        resume_data.setdefault('about', 'Passionate learner ready to grow!')
        resume_data.setdefault('education', 'Not specified')
        resume_data.setdefault('hobbies', '')
        resume_data.setdefault('career', 'Software Developer')
        resume_data.setdefault('summary', 'Aspiring professional with strong foundational skills.')
        resume_data.setdefault('skills', [])
        resume_data.setdefault('photo', url_for('static', filename='profile_photos/default.jpg'))
        
        return render_template('resume.html', resume=resume_data)
    else:
        # Default resume data for new users
        resume_data = {
            'name': 'Student',
            'email': session.get('user', ''),
            'about': 'Passionate learner ready to grow!',
            'education': 'Not specified',
            'hobbies': '',
            'career': 'Software Developer',
            'summary': 'Aspiring professional with strong foundational skills.',
            'skills': [],
            'photo': url_for('static', filename='profile_photos/default.jpg')
        }
        return render_template('resume.html', resume=resume_data)

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

@app.route('/save_profile', methods=['POST'])
def save_profile():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', 'Student')
        email = request.form.get('email', '')
        about = request.form.get('about', 'Passionate learner ready to grow!')
        education = request.form.get('education', 'Not specified')
        hobbies = request.form.get('hobbies', '')
        career = request.form.get('career', 'Software Developer')
        summary = request.form.get('summary', 'Aspiring professional with strong foundational skills.')
        
        # Handle photo upload
        photo_url = None
        if 'photo_upload' in request.files:
            file = request.files['photo_upload']
            if file and allowed_file(file.filename):
                filename = secure_filename(f"{email}_profile.jpg" if email else "default_profile.jpg")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                photo_url = url_for('static', filename=f'profile_photos/{filename}')
        
        # Handle skills
        skills = session.get('user_data', {}).get('skills', [])
        
        # Add new skill
        new_skill = request.form.get('add_skill', '').strip()
        if new_skill and new_skill not in skills:
            skills.append(new_skill)
        
        # Remove skill
        del_skill = request.form.get('del_skill')
        if del_skill and del_skill in skills:
            skills.remove(del_skill)
        
        # Update user data in session
        if 'user_data' in session:
            session['user_data'].update({
                'name': name,
                'email': email,
                'about': about,
                'education': education,
                'hobbies': hobbies,
                'career': career,
                'summary': summary,
                'skills': skills,
                'photo': photo_url if photo_url else session['user_data'].get('photo')
            })
            session.modified = True
        
        flash('Profile saved successfully!', 'success')
        return redirect(url_for('view_profile_card'))

@app.route('/profile_card')
def view_profile_card():
    if 'user_data' in session:
        user_data = session['user_data']
        return render_template('profile_card.html', user=user_data)
    else:
        flash('Please complete your profile first.', 'warning')
        return redirect(url_for('resume'))

@app.route('/resume_edit', methods=['GET', 'POST'])
def resume_edit():
    if request.method == 'POST':
        # ...save profile edits...
        return redirect(url_for('welcome'))
    return render_template('resume_edit.html')  # Create this template

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # Create this template

if __name__ == '__main__':
    app.run(debug=True)

