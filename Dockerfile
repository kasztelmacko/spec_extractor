FROM python:3.12-slim

# 1. Install OS dependencies and clean up in one step
RUN apt-get update && apt-get install -y \
    git \
    curl \
    zstd \
    && rm -rf /var/lib/apt/lists/*

# 2. Download and install Ollama safely with retry, clean up temp files
RUN curl -fsSL --retry 5 -o /tmp/ollama-install.sh https://ollama.com/install.sh \
    && chmod +x /tmp/ollama-install.sh \
    && /tmp/ollama-install.sh \
    && rm -rf /tmp/*

# 3. Set working directory and Python path
WORKDIR /app
ENV PYTHONPATH=/app

# 4. Copy only dependency files first to leverage caching
COPY pyproject.toml ./
RUN pip install --no-cache-dir uv \
    && uv sync

# 5. Copy scripts separately, set executable
COPY scripts/entrypoint.sh /scripts/entrypoint.sh
RUN chmod +x /scripts/entrypoint.sh

# 6. Copy the rest of the app last to avoid invalidating cache unnecessarily
COPY . .

# 7. Entrypoint & default command
ENTRYPOINT ["scripts/entrypoint.sh"]
CMD ["/bin/bash"]
