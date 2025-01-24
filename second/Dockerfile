FROM python:3.9-slim

WORKDIR /app

COPY ./src .

RUN pip install flask gunicorn

EXPOSE 5000

CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "server:app"]