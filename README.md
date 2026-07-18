# 🚀 Enterprise AI-Powered Credit Risk Intelligence Platform

An enterprise-grade Machine Learning platform that predicts loan default risk using the Home Credit Default Risk dataset. The application provides intelligent credit risk prediction through a FastAPI backend and an interactive Streamlit dashboard.

---

# 📌 Project Overview

Financial institutions must accurately identify customers who are likely to default on loans. This project leverages Machine Learning to analyze customer information and generate credit risk predictions.

The platform includes:

- Loan Default Prediction
- Risk Probability Score
- Interactive Dashboard
- REST API
- Docker Support
- Enterprise Project Structure

---

# ✨ Features

- Predict customer loan default risk
- FastAPI REST API
- Streamlit Dashboard
- Data Preprocessing Pipeline
- Feature Engineering
- LightGBM Model
- SHAP Explainability
- Docker Deployment
- Enterprise Folder Structure

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Machine Learning | LightGBM, Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| API | FastAPI |
| Dashboard | Streamlit |
| Deployment | Docker |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
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
├── notebooks/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app.py
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/rahul502mv/Enterprise-Credit-Risk-Platform.git
```

Go into the project

```bash
cd Enterprise-Credit-Risk-Platform
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI

```bash
uvicorn src.api.main:app --reload
```

API:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit

```bash
streamlit run src/dashboard/streamlit_app.py
```

Dashboard:

```
http://localhost:8501
```

---

# 🐳 Docker

Build

```bash
docker build -t credit-risk-platform .
```

Run

```bash
docker run -p 8000:8000 credit-risk-platform
```

---

# 📊 Dataset

Dataset:

Home Credit Default Risk

Target Variable:

```
TARGET
```

Prediction:

```
0 → Non Default

1 → Default
```

---

# 🎯 Future Improvements

- Model Monitoring
- MLflow Integration
- CI/CD Pipeline
- Cloud Deployment
- Authentication
- Model Versioning

---

# 👨‍💻 Author

**Rahul M**

Aspiring Data Scientist

GitHub:

https://github.com/rahul502mv

---

# ⭐ If you like this project

Please consider giving this repository a ⭐