import joblib
from sklearn.linear_model import LinearRegression
import pandas as pd

# Dummy data
data = pd.DataFrame({
    'gpa': [3.5, 3.8, 3.2],
    'test_score': [1500, 1600, 1400],
    'admission': [1, 1, 0]  # 1 = admitted
})

def train_predictor():
    X = data[['gpa', 'test_score']]
    y = data['admission']
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, 'models/predictor_model.pkl')
    print("Predictor trained.")

def predict_admission(profile):
    model = joblib.load('models/predictor_model.pkl')
    pred = model.predict([profile])[0]
    chance = min(max(pred * 100, 0), 100)  # Convert to percentage
    return chance

if __name__ == '__main__':
    train_predictor()
