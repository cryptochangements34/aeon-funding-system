FROM python:3
RUN apt update && apt install python-virtualenv python3 redis-server postgresql-server-dev-* postgresql postgresql-client python-pip virtualenv -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN mv /app/settings_example.py /app/settings.py
CMD ["python","run_dev.py"]