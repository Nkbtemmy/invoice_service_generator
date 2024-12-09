FROM python:3.11.6

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc postgresql-client

# Create and activate a virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install Python packages within the virtual environment
COPY ./requirements*.txt .
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt

# Copy project files into the container
COPY . .

# Run the application with Gunicorn
CMD ["python","manage.py", "runserver"]