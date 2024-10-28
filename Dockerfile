# The base image for python. There are countless official images.
# Alpine just sounded cool.
#
FROM python:3.11-alpine

# The directory in the container where the app will run.
#
WORKDIR /app

# Copy the requirements.txt file from the project directory into the working
# directory and install the requirements.
#
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# Copy over the files.
#
COPY . .

WORKDIR /app/Product_service

# Expose the port the app runs on (if running on 8000)
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]