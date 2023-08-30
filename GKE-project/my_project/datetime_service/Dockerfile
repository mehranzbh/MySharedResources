# Use a base Python image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file to the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local directory to the working directory
COPY datetime_service.py .

# Specify the command to run on container start
CMD ["python", "./datetime_service.py"]

