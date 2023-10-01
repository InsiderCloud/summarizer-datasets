from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.responses import Response
from Cogniezer.pipeline.prediction import PredictionPipeline

prediction_pipeline = PredictionPipeline()
app = FastAPI()


@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs/")

@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response("Training Completed Successfully")
    except Exception as e:
        return Response(e)

@app.post("/predict")
async def predict(text):
    try:
        summary = prediction_pipeline.predict(text)
        return summary
    except Exception as e:
        return Response(e)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
