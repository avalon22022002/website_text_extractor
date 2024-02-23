FROM python:3.7.4

WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port that your Flask app will run on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Command to run your application
CMD ["flask", "run", "--host", "0.0.0.0"]
