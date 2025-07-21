FROM python:3.11-alpine

WORKDIR /app

# Install system and Poetry dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev make curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

ENV POETRY_VIRTUALENVS_CREATE=false

ENV PYTHONPATH=/app

# Start an idle process so container stays alive
CMD ["tail", "-f", "/dev/null"]