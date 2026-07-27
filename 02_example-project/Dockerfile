# ./app/Dockerfile
FROM python:3.11

# Install some operating system applications
RUN apt-get update && apt-get install -y \
    vim \
    man \
 && rm -rf /var/lib/apt/lists/*


# Installs Python dependancies
COPY requirements.txt .

RUN pip install -r requirements.txt

# All Dockerfile commands will be executed from here
WORKDIR /app

COPY ./app .

# Expose HTTP port
EXPOSE 5000

CMD ["python", "webserver.py"]

