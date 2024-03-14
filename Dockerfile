FROM python:3.12.2-slim-bullseye
LABEL authors="Administrator"

ENV HOME=/usr/src/app
WORKDIR $HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock .
COPY pyproject.toml .

RUN pip install  --upgrade pip && pip install poetry --trusted-host pypi.org --trusted-host files.pythonhosted.org  \
    && poetry config virtualenvs.create false  \
    && poetry install

COPY . $APP_HOME