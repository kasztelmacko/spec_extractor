#!/bin/bash

export PYTHONPATH=/app:${PYTHONPATH}

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

