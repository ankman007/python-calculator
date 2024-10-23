# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app/app

# Copy the requirements.txt file first to leverage Docker caching
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app

# Expose the port (if your app exposes one, otherwise skip)
EXPOSE 8000


ENV DB_HOST=db
ENV DB_NAME=calculator_db
ENV DB_USER=user
ENV DB_PASS=password

CMD ["python", "app/main.py"]

