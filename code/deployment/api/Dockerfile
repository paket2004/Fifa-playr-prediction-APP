FROM python:3.9

# Set the working directory in the container
WORKDIR /api

# Copy the requirements file into the container
COPY code/deployment/api /api

# Install the dependencies
RUN pip install --upgrade -r /api/requirements.txt


# Copy the models from the parent folder (deployment) into the container
COPY code/models /api/models

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
