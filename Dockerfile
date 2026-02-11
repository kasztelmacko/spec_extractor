FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    git \
    curl \
    zstd \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL --retry 5 -o /tmp/ollama-install.sh https://ollama.com/install.sh \
    && chmod +x /tmp/ollama-install.sh \
    && /tmp/ollama-install.sh \
    && rm -rf /tmp/*

WORKDIR /app
# Add the uv virtualenv to the PATH so 'python' and 'uv' are always found
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app

COPY pyproject.toml ./
# Install uv and sync dependencies
RUN pip install --no-cache-dir uv && uv sync

# Copy script to a safe location outside of /app to avoid volume overwrite issues
COPY scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY . .

# Use the absolute path to the script
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]