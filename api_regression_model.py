from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

# Create an instance of fast api

app = FastAPI()

# Create a class for requestBody
class request_body(BaseModel):
    study_hours: float

# Load model to do the prediction
score_model = joblib.load('./regression_model.pkl')

@app.post('/predict')
def predict(data: request_body):
    # Prepare data for prediction
    input_feature = [[data.study_hours]]

    # Do the prediction
    y_pred = score_model.predict(input_feature)[0].astype(int)

    return {'score': y_pred.tolist()}


