## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/kasztelmacko/spec_extractor.git
cd spec_extractor
```

### 2. Build and Start Services

Build the Docker images (this will pre-pull the specified Ollama model):

```bash
docker build -t spec_extractor .
```

Start the services:

```bash
docker run -p 7860:7860 spec_extractor
```

Then, after few seconds, enter the url and input you PDF:

```
http://localhost:7860
```


## Prerequisites

- **Docker** and **Docker Compose** installed on your system
- At least 8GB of free disk space (for Ollama models)

- 4GB+ RAM recommended


