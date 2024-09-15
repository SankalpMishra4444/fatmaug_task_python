# Use an official Python runtime as a parent image
FROM python:3.6.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY video_app/requirements.txt /app/

# Install any required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY video_app /app/

# Collect static files (optional, only for production)
# RUN python manage.py collectstatic --noinput

# Expose the port Django will run on
EXPOSE 8000

# Run the Django development server
CMD ["gunicorn", "video_app.wsgi:application", "--bind", "0.0.0.0:8000"]
