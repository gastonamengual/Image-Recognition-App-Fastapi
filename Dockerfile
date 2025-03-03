FROM python:3.12-slim

RUN mkdir build

WORKDIR /build

COPY ./Pipfile ./Pipfile.lock /build/

RUN PIPENV_VENV_IN_PROJECT=1 \
    pip install pipenv && \
    pipenv install --dev


COPY . /build

EXPOSE 8080

WORKDIR /build

CMD ["pipenv", "run", "api"]
