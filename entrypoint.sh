#!/bin/bash

# Activate UV environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "✓ UV environment activated"
else
    echo "⚠ Warning: .venv not found. Run 'uv sync' to create it."
fi

# Execute command or start interactive shell
if [ $# -eq 0 ]; then
    exec /bin/bash
else
    exec "$@"
fi

