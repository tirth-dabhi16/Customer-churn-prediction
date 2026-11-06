# 📊 Customer Churn Prediction System

<p align="center">
  <b>An End-to-End Machine Learning Project with FastAPI & Docker</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/XGBoost-EC6B23?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</p>

## 📌 Overview

Customer churn occurs when customers stop using a company's products or services. Predicting customer churn helps businesses identify customers who are likely to leave and take proactive steps to improve customer retention.

This project develops an end-to-end Machine Learning solution using XGBoost to predict customer churn. It covers the complete ML lifecycle, from data preprocessing and exploratory data analysis to model evaluation and deployment using FastAPI and Docker.

## 🎯 Project Objectives

- Perform Exploratory Data Analysis (EDA) to understand customer behavior.
- Clean and preprocess customer data.
- Apply feature engineering to improve model performance.
- Handle class imbalance using SMOTE.
- Train and compare multiple classification algorithms.
- Optimize the XGBoost model using hyperparameter tuning.
- Evaluate the final model using classification metrics.
- Deploy the trained ML model using FastAPI and Docker.

## ⚙️ Machine Learning Workflow

```text
Data Collection
      |
Data Cleaning & Preprocessing
      |
Exploratory Data Analysis (EDA)
      |
Feature Engineering
      |
Handling Class Imbalance (SMOTE)
      |
Model Training & Comparison
      |
Hyperparameter Tuning
      |
Model Evaluation
      |
Model Serialization (Joblib)
      |
FastAPI Application
      |
Docker Containerization
      |
REST API
```

## 📈 Model Performance

**Final Model:XGBoost Classifier**

The final model was evaluated on 10,000 test samples.

### Performance Metrics

| Metric | Score |
|---|---:|
| Accuracy | **92.36%** |
| Precision | **92.66%** |
| Recall | **79.90%** |
| F1 Score | **85.80%** |
| ROC-AUC | **92.95%** |

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
|---|---:|---:|---:|---:|
| 0 (Non-Churn) | 0.92 | 0.97 | 0.95 | 7,110 |
| 1 (Churn) | 0.93 | 0.80 | 0.86 | 2,890 |
| **Accuracy** | | | 0.92 | 10,000 |
| Macro Avg | 0.92 | 0.89 | 0.90 | 10,000 |
| Weighted Avg | 0.92 | 0.92 | 0.92 | 10,000 |

### 📊 Model Evaluation Highlights

- Achieved **92.36% accuracy** on the test dataset.
- Achieved **92.66% precision**, indicating strong reliability among predicted churn cases.
- Identified approximately **80% of actual churn customers**.
- Achieved a **92.95% ROC-AUC score**, demonstrating strong classification performance.
- Maintained a good balance between precision and recall for churn prediction.

## 🔍 Key Findings

- Lifetime Value was the most important feature (15.16%) for predicting customer churn.
- Customer Service Calls was the second most important feature (13.90%).
- Discount Usage Rate (11.06%) and Cart Abandonment Rate (8.06%) were also important predictors.
- Customer purchasing behavior and engagement-related features contributed to churn prediction.

## 🚀 Model Deployment

The trained machine learning pipeline is serialized using Joblib and integrated into a FastAPI application.

The application exposes a REST API that accepts customer information and returns churn predictions.

### Deployment Architecture

```text
Trained XGBoost Pipeline
          |
        Joblib
          |
     FastAPI App
          |
       Docker
          |
    Docker Compose
          |
   Churn Prediction API
```

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy, Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| API Development | FastAPI |
| Deployment | Docker, Docker Compose |
| Tools | Jupyter Notebook, VS Code |

## 📁 Project Structure

```text
Customer-churn-prediction/
│
├── app/
│   └── main.py
│
├── data/
│
├── notebooks/
│
├── customer_churn_model.pkl
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## 💻 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/tirth-dabhi16/Customer-churn-prediction.git
```

### 2. Navigate to the Project

```bash
cd Customer-churn-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Application

```bash
uvicorn app.main:app --reload
```

### 5. Access API Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Use the interactive Swagger UI to test the customer churn prediction API.

## 🐳 Run with Docker

### Build Docker Image

```bash
docker build -t customer-churn-api .
```

### Run Docker Container

```bash
docker run -d -p 8000:8000 --name customer-churn-api customer-churn-api
```

Access the API:

```text
http://localhost:8000/docs
```

### Run with Docker Compose

Start the application:

```bash
docker compose up -d
```

Stop the application:

```bash
docker compose down
```

## 📚 What I Learned

- Developing end-to-end machine learning pipelines.
- Performing data preprocessing and feature engineering.
- Handling imbalanced datasets using SMOTE.
- Training, comparing, and optimizing classification models.
- Evaluating models using multiple classification metrics.
- Deploying ML models as REST APIs using FastAPI.
- Containerizing machine learning applications using Docker.
- Managing application services using Docker Compose.

## 🔮 Future Improvements

- Deploy the application to a cloud platform.
- Implement CI/CD pipelines.
- Add model monitoring and performance tracking.
- Improve API testing and validation.

## 🙏 Acknowledgement

This project helped me gain practical experience in Data Science and Machine Learning. I learned about data preprocessing, EDA, feature engineering, handling imbalanced datasets, model training, and evaluation.

I also gained hands-on experience in deploying Machine Learning models using FastAPI, Docker, and Docker Compose.

Thank you for visiting this repository! ⭐

## 👨‍💻 Author

**Tirth Dabhi**

Computer Engineering Student | Data Science & AI Enthusiast
