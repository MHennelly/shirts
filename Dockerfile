FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

WORKDIR source

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

EXPOSE 5000