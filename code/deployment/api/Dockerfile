FROM python:3.9

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --upgrade -r /code/requirements.txt

# Copy the application code from api folder into the container
#COPY . /code/api

# Copy the models from the parent folder (deployment) into the container
COPY .. /code

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
