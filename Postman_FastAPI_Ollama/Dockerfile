# ===============================
# Base Image
# ===============================
FROM python:3.13.12

# ===============================
# Environment Variables
# ===============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ===============================
# Set Working Directory
# ===============================
WORKDIR /app

# ===============================
# Copy Requirements
# ===============================
COPY requirements.txt .

# ===============================
# Install Dependencies
# ===============================
RUN pip install --no-cache-dir -r requirements.txt

# ===============================
# Copy Project Files
# ===============================
COPY . .

# ===============================
# Expose Port
# ===============================
EXPOSE 8000

# ===============================
# Start FastAPI App
# ===============================
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]