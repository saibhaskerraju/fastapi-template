#!/bin/bash
set -e

echo "Running in Debug mode on 0.0.0.0:5678"
# tail -f /dev/null
exec python -Xfrozen_modules=off -m debugpy --wait-for-client --listen 0.0.0.0:5678 uvicorn_config.py