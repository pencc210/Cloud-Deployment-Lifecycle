FROM python:3.13-slim
WORKDIR /app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY api.py ./
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# Run the container
# ["python", "api.py"] - JSON style array = to running python api.py on terminal
CMD ["python", "api.py"]  
