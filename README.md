# 🛡️ Insurance Premium Predictor

This project is an interactive web application that predicts insurance premium categories based on user-provided health and demographic data. The application is built with Streamlit and leverages a machine learning model trained on insurance data.

![Insurance Premium Predictor Screenshot](https://i.imgur.com/your-screenshot-code.png)
*Note: Replace the link above with the URL to your own screenshot.*

## 🚀 Live Demo

You can access the live, deployed version of this application on AWS EC2:

**[http://35.154.41.230:8501/](http://35.154.41.230:8501/)**

---

## ✨ Features

-   **Interactive UI**: A user-friendly interface built with Streamlit for easy data entry.
-   **ML Model Integration**: Utilizes a pre-trained `scikit-learn` model to predict premium categories (Low, Medium, High).
-   **Data Validation**: Uses Pantic schemas to validate user input and compute derived features like BMI and age group.
-   **Containerized**: Fully containerized with Docker for consistent deployment and scalability.
-   **Cloud Deployment**: Deployed on an AWS EC2 instance for public access.

---

## 🛠️ How to Run Locally

To run this project on your local machine, follow these steps:

#### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name
```

#### 2. Create and Activate a Virtual Environment
```bash
# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\Activate

# Activate on macOS/Linux
source venv/bin/activate
```

#### 3. Install Dependencies
Install the required packages from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

#### 4. Run the Streamlit App
```bash
streamlit run streamlit_app.py
```
The application will be available at `http://localhost:8501`.

---

## 📂 Project Structure

The project is organized with a clear separation of concerns:

```
.
├── 📄 app.py              # FastAPI application (optional backend)
├── 📄 streamlit_app.py    # Main Streamlit frontend application
├── 📄 dockerfile          # Instructions for building the Docker image
├── 📄 requirements.txt    # Project dependencies
├── 📁 model/
│   ├── 📄 predict.py      # Logic for loading the model and making predictions
│   └── 📄 model.pkl       # The trained machine learning model
├── 📁 schema/
│   ├── 📄 user_input.py   # Pydantic model for user input validation
│   └── 📄 ...
└── 📁 config/
    └── 📄 city_tier.py    # City data configuration
```

---

## 👨‍💻 Made by

**Arsheen Singh**
