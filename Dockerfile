# Use the official Python image
FROM python:3.11-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set the working directory
WORKDIR /app
# Copy the project files
COPY . /app
# Install system dependencies (for matplotlib)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose Streamlit default port
EXPOSE 8501
# Run the Streamlit app
CMD ["streamlit", "run", "voting.py", "--server.port=8501", "--server.enableCORS=false"]