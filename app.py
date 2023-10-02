import uvicorn
import sys
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse,HTMLResponse
from starlette.responses import Response
from fastapi.staticfiles import StaticFiles
from Cogniezer.pipeline.prediction import PredictionPipeline
from Cogniezer.pipeline.transcribe import TranscribePipeline

prediction_pipeline = PredictionPipeline()
transcribe_pipeline = TranscribePipeline()
app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/",tags=["authentication"])
async def index():
    return HTMLResponse(content=templates.get_template("index.html").render(), status_code=200)
    

@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response("Training Completed Successfully")
    except Exception as e:
        return Response(e)

@app.post("/api/predict")
async def predict(text):
    try:
        summary = prediction_pipeline.predict(text)
        return summary
    except Exception as e:
        return Response(e)

@app.post("/api/uploadfile/")
async def upload_file(file: UploadFile):
    file_path = os.path.join("audio-uploads", file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    try:
        text = transcribe_pipeline.transcribe(file_path)
        summary = prediction_pipeline.predict(text)
        return summary
    except Exception as e:
        return Response(e)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
