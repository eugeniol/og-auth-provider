FROM python:alpine

WORKDIR /app
ADD . .
RUN apk add --no-cache py-cryptography && pip freeze

CMD ["python", "oauth3/manage.py", "runserver", "0.0.0.0:8080"]
