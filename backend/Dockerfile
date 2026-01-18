FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the model file from the parent/model directory (context context will handle this)
COPY . . 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]