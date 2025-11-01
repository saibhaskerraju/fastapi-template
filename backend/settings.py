import os

ENV_MODE = os.getenv("ENV_MODE", "local")

PORT = int(os.getenv("PORT", 8000))
HOST = os.getenv("HOST", "0.0.0.0")
