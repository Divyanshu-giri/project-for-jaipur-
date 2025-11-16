from flask import Blueprint, render_template, request, jsonify
from models.skill_assessment import predict_skills
from models.recommender import recommend_courses
from models.predictor import predict_admission

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/skill-assessment', methods=['GET', 'POST'])
def skill_assessment():
    if request.method == 'POST':
        data = request.json
        skills = [data.get('python_skill', 0), data.get('ml_skill', 0)]
        career = predict_skills(skills)
        result = {"career": career, "recommendations": ["Improve Python", "Learn ML"]}
        return jsonify(result)
    return render_template('skill_assessment.html')

@bp.route('/resume-builder', methods=['GET', 'POST'])
def resume_builder():
    if request.method == 'POST':
        # Placeholder for NLP logic
        data = request.json
        # Generate resume
        resume = {"content": "Generated resume text"}
        return jsonify(resume)
    return render_template('resume_builder.html')

@bp.route('/mentor-matching')
def mentor_matching():
    # Placeholder
    mentors = [{"name": "John Doe", "expertise": "Data Science"}]
    return render_template('mentor_matching.html', mentors=mentors)

@bp.route('/interview-simulator')
def interview_simulator():
    return render_template('interview_simulator.html')

@bp.route('/job-board')
def job_board():
    # Placeholder for scraped jobs
    jobs = [{"title": "Data Scientist", "company": "ABC Corp"}]
    return render_template('job_board.html', jobs=jobs)

@bp.route('/course-recommender', methods=['GET', 'POST'])
def course_recommender():
    if request.method == 'POST':
        data = request.json
        # ML recommendation
        courses = ["Machine Learning on Coursera", "Python for Data Science"]
        return jsonify(courses)
    return render_template('course_recommender.html')

@bp.route('/admission-predictor', methods=['GET', 'POST'])
def admission_predictor():
    if request.method == 'POST':
        data = request.json
        # ML prediction
        prediction = {"chance": 75}
        return jsonify(prediction)
    return render_template('admission_predictor.html')
