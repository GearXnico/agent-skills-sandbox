FROM python:3.13-slim
RUN pip install --no-cache-dir poetry==2.1.3
WORKDIR /app
COPY pyproject.toml poetry.lock ./
COPY src ./src
RUN poetry config virtualenvs.create false && poetry install --only main
ENTRYPOINT ["wordcount"]
