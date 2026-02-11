FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl zstd && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
ENV PYTHONPATH="/app"
ENV GRADIO_SERVER_NAME="0.0.0.0"

COPY pyproject.toml .
RUN uv sync

RUN ollama serve & sleep 10 && ollama pull llama3.2

COPY . .

CMD ["sh", "-c", "ollama serve & .venv/bin/python src/app/gradio_app.py"]