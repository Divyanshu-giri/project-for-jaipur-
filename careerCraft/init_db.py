#!/usr/bin/env python3
"""
Database initialization script for CareerCraft
"""
import os
import sys
from app import app, db

def init_database():
    """Initialize the database by creating all tables"""
    print("Initializing CareerCraft database...")
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # List all available tables
        tables = [t.name for t in db.metadata.tables.values()]
        print(f"Available tables: {tables}")

if __name__ == '__main__':
    init_database()
