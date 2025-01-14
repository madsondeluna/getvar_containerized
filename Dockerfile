# Use Python 3.8 as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point to run the Flask application
CMD ["python", "main.py"]
