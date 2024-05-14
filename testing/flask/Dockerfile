FROM python:3.11-alpine

ENV APP_PORT=5000

WORKDIR /app
ADD  requirements.txt .
ADD *.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE ${APP_PORT}

ENTRYPOINT ["flask"]
CMD ["--app", "main", "run", "--host", "0.0.0.0", "--port", ${APP_PORT}]