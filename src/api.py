from fastapi import FastAPI
from src.recommend import recommend

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/recommend/{product}")
def get_recommendations(product: str):

    results = recommend(product)

    return {
        "product": product,
        "recommendations": results
    }