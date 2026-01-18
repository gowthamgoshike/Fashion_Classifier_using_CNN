from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
import os

# Get the folder where this script (main.py) is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to the model file
model_path = os.path.join(script_dir, "fashion_model.h5")

# Load the model
model = tf.keras.models.load_model(model_path)
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

app = FastAPI()

def preprocess_image(image: Image.Image):
    image = image.resize((28, 28)).convert('L') # Resize and convert to grayscale
    image_np = np.array(image) / 255.0          # Normalize
    image_np = image_np.reshape(1, 28, 28, 1)   # Batch dimension
    return image_np

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(BytesIO(image_data))
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    
    predicted_class = class_names[np.argmax(prediction)]
    confidence = float(np.max(prediction))
    
    return {"class": predicted_class, "confidence": confidence}