#!/bin/bash

export PYTHONPATH=/app:${PYTHONPATH}

# Configure Git with GitHub token if provided
if [ -n "$GITHUB_TOKEN" ]; then
    # Configure Git credential helper to use token
    git config --global credential.helper store
    # Create credential file with token
    echo "https://${GITHUB_TOKEN}@github.com" > /root/.git-credentials
    chmod 600 /root/.git-credentials
    # Configure Git user if provided
    if [ -n "$GITHUB_USER" ]; then
        git config --global user.name "$GITHUB_USER"
    fi
    if [ -n "$GITHUB_EMAIL" ]; then
        git config --global user.email "$GITHUB_EMAIL"
    fi
    echo "✓ GitHub authentication configured"
fi

if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "✓ UV environment activated"
else
    echo "⚠ .venv not found. Creating it with 'uv sync'..."
    uv sync
    if [ -d ".venv" ]; then
        source .venv/bin/activate
        echo "✓ UV environment created and activated"
    else
        echo "✗ Failed to create .venv"
    fi
fi

if [ $# -eq 0 ]; then
    exec /bin/bash -i
else
    exec "$@"
fi

