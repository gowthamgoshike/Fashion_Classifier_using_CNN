import streamlit as st
import requests
from PIL import Image

st.title("👕 Fashion MNIST Classifier")
st.write("Upload an image of a clothing item to identify it!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    if st.button('Predict'):
        # Send to API
        files = {"file": uploaded_file.getvalue()}
        # Note: "backend" is the hostname in Docker Compose
        #res = requests.post("http://127.0.0.1:8000/predict", files=files)
        res = requests.post("http://backend:8000/predict", files=files)

        if res.status_code == 200:
            result = res.json()
            st.success(f"Prediction: **{result['class']}**")
            st.info(f"Confidence: {result['confidence']:.2%}")
        else:
            st.error("Error connecting to the API")