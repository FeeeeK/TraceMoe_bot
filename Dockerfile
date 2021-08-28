FROM python:3.8-slim

WORKDIR /tracemoe_bot

RUN pip install poetry

COPY pyproject.toml ./
RUN poetry install

COPY __main__.py ./
COPY config ./
COPY src ./
