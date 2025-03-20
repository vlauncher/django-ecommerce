# Use an official lightweight Python image.
FROM python:3.13-bullseye

# Prevent Python from writing .pyc files and buffering stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies.
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies.
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project files.
COPY . /app/

# Expose port 8000 for the application.
EXPOSE 8000

# Use Gunicorn as the WSGI server.
CMD ["gunicorn", "ecommerce_project.wsgi:application", "--bind", "0.0.0.0:8000"]
