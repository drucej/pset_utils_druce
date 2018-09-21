FROM python:3.6 AS base
ENV PIP_NO_CACHE_DIR off
ENV PYTHONPATH="/app:${PYTHONPATH}";
RUN pip3 install pipenv
RUN pip3 install setuptools_scm

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --dev