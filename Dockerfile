FROM python:3.8-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install --trusted-host pypi.org --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
CMD python app.py