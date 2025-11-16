import joblib
from sklearn.neighbors import NearestNeighbors
import pandas as pd

# Dummy course data
courses = pd.DataFrame({
    'course_id': [1, 2, 3],
    'title': ['Python Basics', 'ML with TensorFlow', 'Data Analysis'],
    'features': [[1,0,0], [0,1,1], [1,1,0]]  # e.g., beginner, advanced, etc.
})

def train_recommender():
    model = NearestNeighbors(n_neighbors=2)
    model.fit(courses['features'].tolist())
    joblib.dump(model, 'models/recommender_model.pkl')
    print("Recommender trained.")

def recommend_courses(user_features):
    model = joblib.load('models/recommender_model.pkl')
    distances, indices = model.kneighbors([user_features])
    recommended = courses.iloc[indices[0]]['title'].tolist()
    return recommended

if __name__ == '__main__':
    train_recommender()
