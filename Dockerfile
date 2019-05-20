FROM python:3.7

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-interaction
RUN poetry shell
COPY . /app

CMD ["waitress-serve", "--port", "5000", "--call", "vnsegapi.server:make_app"]
