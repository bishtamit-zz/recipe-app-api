FROM python:3.8.6-slim
MAINTAINER amit bisht

WORKDIR /app
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app /app

RUN useradd -m user
USER user
