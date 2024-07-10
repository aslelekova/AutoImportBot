FROM ubuntu:20.04

# Install necessary packages using apt-get and update the package list
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install project dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

# Copy project files into the Docker image
COPY . /app

# Define the entry point to run the bot
CMD ["python3", "main.py"]
