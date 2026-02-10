FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    git \
    curl \
    zstd \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install --no-cache-dir uv

WORKDIR /app
ENV PYTHONPATH=/app

COPY pyproject.toml ./
RUN uv sync

COPY scripts/entrypoint.sh /scripts/entrypoint.sh
RUN chmod +x /scripts/entrypoint.sh

COPY . .

ENTRYPOINT ["scripts/entrypoint.sh"]
CMD ["/bin/bash"]
