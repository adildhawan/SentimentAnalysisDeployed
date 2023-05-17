from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel

# Load your model, vectorizer, and encoder
model = load('sentiment_model.joblib')
vectorizer = load('vectorizer.joblib')
encoder = load('encoder.joblib')

app = FastAPI()

class Item(BaseModel):
    text: str

@app.post('/predict')
def predict(item: Item):
    text_data = item.text
    vectorized_text = vectorizer.transform([text_data])
    prediction = model.predict(vectorized_text)
    sentiment = encoder.inverse_transform(prediction)
    return {'prediction': sentiment[0]}
