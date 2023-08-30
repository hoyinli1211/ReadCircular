# Pull base image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download spacy model
RUN python -m spacy download en_core_web_sm

# Copy project
COPY . /app/

# Expose port
EXPOSE 8501

# Run the application:
CMD streamlit run App.py
