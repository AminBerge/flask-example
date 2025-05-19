# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Copy the application code
COPY . .

# Use non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]