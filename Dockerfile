FROM python:3.11-slim

# ---------------------------------------
# Working Directory
# ---------------------------------------

WORKDIR /app

# ---------------------------------------
# Linux Dependencies
# ---------------------------------------

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------
# Python Path
# ---------------------------------------

ENV PYTHONPATH=/app

# ---------------------------------------
# Install Requirements
# ---------------------------------------

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# ---------------------------------------
# Copy Project
# ---------------------------------------

COPY . .

# ---------------------------------------
# Ports
# ---------------------------------------

EXPOSE 8000
EXPOSE 8501

# ---------------------------------------
# Start FastAPI + Streamlit
# ---------------------------------------

CMD ["sh", "-c", "uvicorn src.api.main:app --host 0.0.0.0 --port 8000 & python -m streamlit run src/dashboard/streamlit_app.py --server.address 0.0.0.0 --server.port 8501"]