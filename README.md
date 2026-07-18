# 🚀 Enterprise AI-Powered Credit Risk Intelligence Platform

An enterprise-grade Machine Learning platform that predicts customer loan default risk using the Home Credit Default Risk dataset. The platform combines **Machine Learning**, **FastAPI**, **Streamlit**, **Docker**, and **Render Cloud** to provide a production-style end-to-end credit risk prediction solution.

---

# 🌐 Live Demo

## 📊 Streamlit Dashboard

**Live Dashboard**

https://enterprise-credit-risk-dashboard.onrender.com

---

## ⚡ FastAPI REST API

**Live API**

https://enterprise-credit-risk-platform.onrender.com

---

## 📄 API Documentation (Swagger)

https://enterprise-credit-risk-platform.onrender.com/docs

---

# 📌 Project Overview

Financial institutions face significant challenges in identifying customers who are likely to default on loans.

This project uses Machine Learning to analyze customer information and predict the probability of loan default.

The platform has been designed following enterprise software development practices and deployed on the cloud using Docker and Render.

---

# ✨ Features

- Loan Default Prediction
- Credit Risk Classification
- FastAPI REST API
- Interactive Streamlit Dashboard
- Data Preprocessing Pipeline
- Feature Engineering
- LightGBM Machine Learning Model
- Explainable AI Ready (SHAP)
- Dockerized Application
- Cloud Deployment using Render
- Production-style Project Structure

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Machine Learning | LightGBM, Scikit-learn |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib, Plotly |
| API | FastAPI |
| Dashboard | Streamlit |
| Deployment | Docker, Render |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
Enterprise-Credit-Risk-Platform/
│
├── src/
│   ├── api/
│   ├── dashboard/
│   ├── explainability/
│   ├── models/
│   ├── preprocessing/
│   ├── recommendation/
│   └── utils/
│
├── saved_models/
├── notebooks/
├── tests/
│
├── Dockerfile
├── Dockerfile.streamlit
├── docker-compose.yml
├── requirements.txt
├── app.py
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/rahul502mv/Enterprise-Credit-Risk-Platform.git
```

Go to project folder

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

Install Dependencies

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

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶ Run Streamlit Dashboard

```bash
streamlit run src/dashboard/streamlit_app.py
```

Open

```
http://localhost:8501
```

---

# 🐳 Docker

Build Image

```bash
docker build -t enterprise-credit-risk .
```

Run Container

```bash
docker run -p 8000:8000 enterprise-credit-risk
```

---

# 📊 Dataset

Dataset Used

**Home Credit Default Risk**

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

## FastAPI

https://enterprise-credit-risk-platform.onrender.com

---

## Streamlit Dashboard

https://enterprise-credit-risk-dashboard.onrender.com

---

# 📈 Machine Learning Pipeline

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Feature Scaling
- LightGBM Training
- Prediction Pipeline
- Risk Classification
- Dashboard Visualization

---

# 📷 Project Screenshots

Add screenshots inside an `images/` folder.

Example:

```markdown
![Dashboard](images/dashboard.png)
```

---

# 🎯 Future Improvements

- SHAP Explainability Dashboard
- MLflow Integration
- Authentication System
- Prediction History
- PDF Report Generation
- CI/CD Pipeline
- Kubernetes Deployment
- AWS / Azure Deployment

---

# 👨‍💻 Author

**Rahul M**

Aspiring Data Scientist

GitHub

https://github.com/rahul502mv

LinkedIn

(Add your LinkedIn profile URL here)

---

# ⭐ Support

If you found this project useful,

Please consider giving this repository a ⭐ on GitHub.

---

# 📜 License

This project is created for educational, portfolio, and research purposes.