# Start from a Python image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy over the python files and requirements
COPY ./RepoToText.py /app
COPY ./requirements.txt /app

# Install the python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the server
EXPOSE 5000

# Start the server
CMD ["python", "RepoToText.py"]
