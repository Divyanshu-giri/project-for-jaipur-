import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Dummy data for training
def train_model():
    # Sample data: features like python_skill, ml_skill, etc., target career
    data = {
        'python_skill': [1, 0, 1, 0, 1],
        'ml_skill': [1, 1, 0, 0, 1],
        'career': ['Data Scientist', 'Engineer', 'Analyst', 'Manager', 'Scientist']
    }
    df = pd.DataFrame(data)
    X = df[['python_skill', 'ml_skill']]
    y = df['career']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, 'models/skill_model.pkl')
    print("Model trained and saved.")

def predict_skills(skills):
    model = joblib.load('models/skill_model.pkl')
    prediction = model.predict([skills])
    return prediction[0]

# Train on import
if __name__ == '__main__':
    train_model()
