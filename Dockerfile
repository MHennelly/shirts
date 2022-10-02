FROM python:3.10-slim-buster

RUN apt update && \
    apt upgrade -y && \
    apt install -y gcc libpq-dev && \
    apt clean

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY ./source /usr/src/app/source

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "source.app:app"]

EXPOSE 5000
