# 👕 Fashion MNIST Image Classifier (End-to-End Deep Learning App)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

## 📌 Project Overview
This project is a **Full Stack Data Science Application** that classifies images of clothing items into 10 distinct categories (e.g., T-shirts, Sneakers, Bags) using a **Convolutional Neural Network (CNN)**.

Unlike a standard Jupyter Notebook project, this application is production-ready. It decouples the **Model**, **API**, and **User Interface** into separate microservices, all containerized using **Docker** for easy deployment.

### 🏗️ Architecture
The project follows a microservices architecture:
1.  **Model Layer:** A CNN trained on the Fashion MNIST dataset using **TensorFlow/Keras**.
2.  **Backend Layer:** A **FastAPI** server that exposes the model via a RESTful API endpoint.
3.  **Frontend Layer:** A **Streamlit** web interface that allows users to upload images and visualize predictions.
4.  **DevOps:** The entire stack is orchestrated using **Docker Compose**.

---

## 🛠️ Tech Stack
* **Deep Learning:** TensorFlow, Keras, NumPy
* **Backend:** FastAPI, Uvicorn, Python-Multipart
* **Frontend:** Streamlit, Requests, Pillow
* **Containerization:** Docker, Docker Compose

---

## 🚀 How to Run the Project

### Option 1: Using Docker (Recommended)
This method requires **Docker Desktop** installed. It guarantees the app runs exactly as intended without dependency issues.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/fashion-classifier.git](https://github.com/your-username/fashion-classifier.git)
    cd fashion-classifier
    ```

2.  **Train the Model (One-time setup):**
    Before building the containers, generate the trained model file.
    ```bash
    pip install tensorflow numpy
    python model/train.py
    ```

3.  **Build and Run:**
    ```bash
    docker-compose up --build
    ```

4.  **Access the Application:**
    * **Frontend UI:** Open [http://localhost:8501](http://localhost:8501) in your browser.
    * **API Docs:** Open [http://localhost:8000/docs](http://localhost:8000/docs).

### Option 2: Running Manually (Local)
If you do not have Docker, you can run the services in separate terminals.

1.  **Train the Model:**
    ```bash
    python model/train.py
    ```

2.  **Start the Backend:**
    ```bash
    cd backend
    pip install -r requirements.txt
    # Copy the model to the backend folder
    cp ../model/fashion_model.h5 . 
    uvicorn main:app --reload --port 8000
    ```

3.  **Start the Frontend:**
    *(Open a new terminal)*
    ```bash
    cd frontend
    pip install -r requirements.txt
    streamlit run app.py
    ```

---

## 📡 API Documentation

### POST `/predict`
Accepts an image file and returns the predicted class and confidence score.

* **Request:** `multipart/form-data`
    * Key: `file` (Image file: jpg, png)
* **Response:** JSON
    ```json
    {
      "class": "Sneaker",
      "confidence": 0.985
    }
    ```

---

## 📂 Project Structure

```text
fashion_classifier/
├── model/
│   ├── train.py           # Script to train CNN and save .h5 model
│   └── fashion_model.h5   # Trained model artifact
├── backend/
│   ├── Dockerfile         # API container config
│   ├── main.py            # FastAPI application logic
│   └── requirements.txt   # Backend dependencies
├── frontend/
│   ├── Dockerfile         # UI container config
│   ├── app.py             # Streamlit interface
│   └── requirements.txt   # Frontend dependencies
├── docker-compose.yml     # Container orchestration
└── README.md              # Project documentation
