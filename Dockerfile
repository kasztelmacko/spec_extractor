FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    git \
    curl \
    zstd \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml ./
COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN uv sync

RUN echo 'if [ -d "/app/.venv" ]; then\n\
    source /app/.venv/bin/activate\n\
    echo "✓ UV environment activated"\n\
fi' >> /root/.bashrc

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]

