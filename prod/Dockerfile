# Dockerfile to run your Python script (expects script.py in the build context)
FROM python:3.11-slim

WORKDIR /app

# Copy project files
COPY . /app

# Default command to start the Python script (change script.py if needed)
CMD ["python", "script.py"]