# wordcount

Counts the words in a text file.

## Development

```sh
pip install poetry
poetry install
poetry run pytest -q
poetry run wordcount README.md
```

## Docker

```sh
docker build -t wordcount .
docker run --rm -v "$PWD:/data" wordcount /data/README.md
```
