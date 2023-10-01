FROM python:3.10.1-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install transformers transformers[sentencepiece] datasets matplotlib torch notebook sacrebleu  rouge_score  py7zr pandas nltk tqdm PyYAML boto3 mypy-boto3-s3 python-box==6.0.2 ensure==1.0.2 fastapi==0.78.0 uvicorn==0.18.3 Jinja2==3.1.2 python-multipart azure-cognitiveservices-speech python-dotenv gunicorn
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python3", "app.py"]
