FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the required files
COPY requirements.txt .
COPY ledger.py .
COPY ledger_api_server.py .

# Assuming your script is named main.py
COPY main.py .  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by the API server
EXPOSE 8000

# Command to run the application
CMD ["python", "/app/main.py"]
