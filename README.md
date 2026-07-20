# 🚀 Enterprise AI-Powered Credit Risk Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.46-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

# 🚀 Enterprise AI-Powered Credit Risk Intelligence Platform

An enterprise-grade Machine Learning application that predicts customer loan default risk using the Home Credit Default Risk dataset. This project demonstrates an end-to-end ML workflow including preprocessing, model training, REST API development, interactive dashboard creation, containerization, and cloud deployment.

---

# 🌐 Live Demo

## 📊 Streamlit Dashboard

🔗 https://enterprise-credit-risk-dashboard.onrender.com

---

## ⚡ FastAPI REST API

🔗 https://enterprise-credit-risk-platform.onrender.com

---

## 📄 Swagger API Documentation

🔗 https://enterprise-credit-risk-platform.onrender.com/docs

---

# 📷 Project Screenshot

## Streamlit Dashboard

![Dashboard](images/dashboard.png)

---

# 📌 Project Overview

This project helps financial institutions predict whether a customer is likely to default on a loan.

It follows enterprise software development practices and is deployed using Docker and Render Cloud.

---

# ✨ Features

- Loan Default Prediction
- Credit Risk Analysis
- CSV File Upload
- Dataset Preview
- Machine Learning Prediction
- FastAPI REST API
- Interactive Streamlit Dashboard
- Docker Support
- Cloud Deployment
- Enterprise Project Structure

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Machine Learning | LightGBM, Scikit-learn |
| Data Processing | Pandas, NumPy |
| API | FastAPI |
| Dashboard | Streamlit |
| Visualization | Plotly, Matplotlib |
| Deployment | Docker, Render |
| Version Control | Git, GitHub |

---

# 📂 Project Structure

```text
Enterprise-Credit-Risk-Platform/
│
├── images/
│   └── dashboard.png
│
├── notebooks/
├── saved_models/
├── src/
│   ├── api/
│   ├── dashboard/
│   ├── models/
│   ├── preprocessing/
│   ├── recommendation/
│   └── utils/
│
├── tests/
├── Dockerfile
├── Dockerfile.streamlit
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/rahul502mv/Enterprise-Credit-Risk-Platform.git
```

Go to project

```bash
cd Enterprise-Credit-Risk-Platform
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run FastAPI

```bash
uvicorn src.api.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# ▶ Run Streamlit

```bash
streamlit run src/dashboard/streamlit_app.py
```

Open

```
http://localhost:8501
```

---

# 🐳 Docker

Build

```bash
docker build -t enterprise-credit-risk .
```

Run

```bash
docker run -p 8000:8000 enterprise-credit-risk
```

---

# 📊 Dataset

Dataset:

Home Credit Default Risk

Target Variable

```
TARGET
```

Prediction

```
0 → Non Default

1 → Default
```

---

# 🚀 Deployment

### Streamlit Dashboard

https://enterprise-credit-risk-dashboard.onrender.com

### FastAPI

https://enterprise-credit-risk-platform.onrender.com

### Swagger

https://enterprise-credit-risk-platform.onrender.com/docs

---

# 📈 Machine Learning Pipeline

- Data Cleaning
- Missing Value Imputation
- Feature Engineering
- Feature Scaling
- LightGBM Model
- Prediction Pipeline
- REST API
- Streamlit Dashboard
- Docker Deployment
- Cloud Deployment

---

# 🎯 Future Improvements

- SHAP Explainability
- MLflow
- Authentication
- PDF Report
- Prediction History
- CI/CD Pipeline
- Kubernetes Deployment
- AWS Deployment

---

# 👨‍💻 Author

**Rahul M**

Aspiring Data Scientist

GitHub

https://github.com/rahul502mv

---

# ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

---

# 📜 License

This project is created for educational, research, and portfolio purposes.
