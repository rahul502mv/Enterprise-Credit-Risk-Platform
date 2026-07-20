# 🚀 Enterprise AI-Powered Credit Risk Intelligence Platform

An enterprise-grade Machine Learning application that predicts customer
loan default risk using the Home Credit Default Risk dataset. This
project demonstrates an end-to-end ML workflow including preprocessing,
model training, REST API development, interactive dashboard creation,
containerization, and cloud deployment.

------------------------------------------------------------------------

# 🌐 Live Demo

## 📊 Streamlit Dashboard

🔗 https://enterprise-credit-risk-dashboard.onrender.com

## ⚡ FastAPI REST API

🔗 https://enterprise-credit-risk-platform.onrender.com

## 📄 Swagger API Documentation

🔗 https://enterprise-credit-risk-platform.onrender.com/docs

------------------------------------------------------------------------

# 📷 Project Screenshot

![Dashboard](images/dashboard.png)

------------------------------------------------------------------------

# 📌 Project Overview

This project helps financial institutions predict whether a customer is
likely to default on a loan. It follows enterprise software development
practices and is deployed using Docker and Render Cloud.

------------------------------------------------------------------------

# ✨ Features

-   Loan Default Prediction
-   Credit Risk Analysis
-   CSV File Upload
-   Dataset Preview
-   Machine Learning Prediction
-   FastAPI REST API
-   Interactive Streamlit Dashboard
-   Docker Support
-   Cloud Deployment
-   Enterprise Project Structure

------------------------------------------------------------------------

# 🛠 Technology Stack

  Category           Technology
  ------------------ ------------------------
  Language           Python
  Machine Learning   LightGBM, Scikit-learn
  Data Processing    Pandas, NumPy
  API                FastAPI
  Dashboard          Streamlit
  Visualization      Plotly, Matplotlib
  Deployment         Docker, Render
  Version Control    Git, GitHub

------------------------------------------------------------------------

# 📂 Project Structure

``` text
Enterprise-Credit-Risk-Platform/
├── images/
├── notebooks/
├── saved_models/
├── src/
├── Dockerfile
├── Dockerfile.streamlit
├── docker-compose.yml
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

# ⚙ Installation

``` bash
git clone https://github.com/rahul502mv/Enterprise-Credit-Risk-Platform.git
cd Enterprise-Credit-Risk-Platform
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

------------------------------------------------------------------------

# ▶ Run FastAPI

``` bash
uvicorn src.api.main:app --reload
```

# ▶ Run Streamlit

``` bash
streamlit run src/dashboard/streamlit_app.py
```

------------------------------------------------------------------------

# 🐳 Docker

``` bash
docker build -t enterprise-credit-risk .
docker run -p 8000:8000 enterprise-credit-risk
```

------------------------------------------------------------------------

# 📊 Dataset

-   Dataset: Home Credit Default Risk
-   Target: TARGET
-   0 → Non Default
-   1 → Default

------------------------------------------------------------------------

# 🚀 Deployment

-   Streamlit: https://enterprise-credit-risk-dashboard.onrender.com
-   FastAPI: https://enterprise-credit-risk-platform.onrender.com
-   Swagger: https://enterprise-credit-risk-platform.onrender.com/docs

------------------------------------------------------------------------

# 📈 Machine Learning Pipeline

-   Data Cleaning
-   Missing Value Imputation
-   Feature Engineering
-   Feature Scaling
-   LightGBM
-   Prediction Pipeline
-   REST API
-   Streamlit
-   Docker
-   Cloud Deployment

------------------------------------------------------------------------

# 🎯 Future Improvements

-   SHAP Explainability
-   MLflow
-   Authentication
-   PDF Report
-   Prediction History
-   CI/CD Pipeline
-   Kubernetes
-   AWS

------------------------------------------------------------------------

# 👨‍💻 Author

**Rahul M**

Aspiring Data Scientist

GitHub: https://github.com/rahul502mv

------------------------------------------------------------------------

# ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

------------------------------------------------------------------------

# 📜 License

This project is created for educational, research, and portfolio
purposes.
