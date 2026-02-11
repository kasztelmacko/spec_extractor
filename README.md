## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/kasztelmacko/spec_extractor.git
cd spec_extractor
```

### 2. Configure Environment

Copy a `.env.example` file as `.env` into the project root. The following settings can customized. **Creating .env file is necessary for running the project**, but changin parameters is not:

```bash
OLLAMA_MODEL=llama3.2
GITHUB_TOKEN=token

GITHUB_USER=username
GITHUB_EMAIL=email
```

If you don't create a `.env` file, the default model (`llama3.2`) will be used.

### 3. Build and Start Services

Build the Docker images (this will pre-pull the specified Ollama model):

```bash
docker-compose build
```

Start the services:

```bash
docker-compose up -d
```

This will start:
- **Ollama service**: LLM inference server with the model pre-pulled
- **spec-extractor service**: Application container

### 4. Run the Extraction

Enter the application container:

```bash
docker-compose exec spec-extractor bash
```

Run the gradio app:

```bash
uv run python src/app/gradio_app.py
```

Inside the app input a PDF to extract specifications from.

## Configuration

### Environment Variables

You can configure the following via `.env` file or environment variables:

- **`OLLAMA_MODEL`**: The Ollama model to use (default: `llama3.2`)
  - Examples: `llama3.2`, `llama3.1`, `mistral`, `llama2`
- **`GITHUB_TOKEN`**: Personal access token for github
- **`GITHUB_USER`**: Github username
- **`GITHUB_EMAIL`**: Github email

### Changing the Model

1. Update `.env` file:
   ```bash
   OLLAMA_MODEL=llama3.1
   ```

2. Rebuild the Ollama service:
   ```bash
   docker-compose build ollama
   docker-compose up -d ollama
   ```

## Prerequisites

- **Docker** and **Docker Compose** installed on your system
- At least 8GB of free disk space (for Ollama models)

- 4GB+ RAM recommended
