from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), nullable=False, default='Student')
    phone = db.Column(db.String(20))
    career_field = db.Column(db.String(100), default='Software Developer')
    hobbies = db.Column(db.Text)
    about = db.Column(db.Text)
    education = db.Column(db.Text)
    summary = db.Column(db.Text)
    photo = db.Column(db.String(200))
    score = db.Column(db.Integer, default=0)
    level = db.Column(db.String(50), default='Beginner')
    xp = db.Column(db.Integer, default=0)
    badges = db.Column(db.Text, default=json.dumps([]))
    skills = db.Column(db.Text, default=json.dumps([]))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    progress = db.relationship('UserProgress', backref='user', lazy=True)
    mentor_connections = db.relationship('MentorConnection', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_skills(self):
        return json.loads(self.skills) if self.skills else []
    
    def set_skills(self, skills_list):
        self.skills = json.dumps(skills_list)
    
    def get_badges(self):
        return json.loads(self.badges) if self.badges else []
    
    def set_badges(self, badges_list):
        self.badges = json.dumps(badges_list)
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'phone': self.phone,
            'career_field': self.career_field,
            'hobbies': self.hobbies,
            'about': self.about,
            'education': self.education,
            'summary': self.summary,
            'photo': self.photo,
            'score': self.score,
            'level': self.level,
            'xp': self.xp,
            'skills': self.get_skills(),
            'badges': self.get_badges(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class UserProgress(db.Model):
    __tablename__ = 'user_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action_type = db.Column(db.String(50), nullable=False)  # quiz_completed, resume_generated, etc.
    action_data = db.Column(db.Text)
    xp_earned = db.Column(db.Integer, default=0)
    badge_earned = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Mentor(db.Model):
    __tablename__ = 'mentors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    field = db.Column(db.String(100), nullable=False)
    expertise = db.Column(db.Text)
    bio = db.Column(db.Text)
    photo = db.Column(db.String(200))
    min_score = db.Column(db.Integer, default=0)
    max_score = db.Column(db.Integer, default=20)
    availability = db.Column(db.Text)
    rating = db.Column(db.Float, default=0.0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    connections = db.relationship('MentorConnection', backref='mentor', lazy=True)

class MentorConnection(db.Model):
    __tablename__ = 'mentor_connections'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentors.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected, completed
    meeting_date = db.Column(db.DateTime)
    notes = db.Column(db.Text)
    rating = db.Column(db.Integer)
    feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Job(db.Model):
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100))
    domain = db.Column(db.String(100))
    description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    min_score = db.Column(db.Integer, default=0)
    max_score = db.Column(db.Integer, default=20)
    salary_range = db.Column(db.String(100))
    application_url = db.Column(db.String(500))
    is_active = db.Column(db.Boolean, default=True)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    provider = db.Column(db.String(100))
    url = db.Column(db.String(500), nullable=False)
    field = db.Column(db.String(100))
    difficulty = db.Column(db.String(50))  # beginner, intermediate, advanced
    duration = db.Column(db.String(100))
    rating = db.Column(db.Float)
    is_free = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)

class RoadmapStep(db.Model):
    __tablename__ = 'roadmap_steps'
    
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(100), nullable=False)
    step_number = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    resources = db.Column(db.Text)  # JSON string of resource links
    estimated_time = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True)
    
    __table_args__ = (db.UniqueConstraint('field', 'step_number', name='_field_step_uc'),)
