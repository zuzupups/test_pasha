FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install flask gunicorn
CMD gunicorn -b 0.0.0.0 app:app