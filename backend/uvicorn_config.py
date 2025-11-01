import os

import uvicorn

from settings import ENV_MODE, HOST, PORT

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        log_level="info",
        reload=ENV_MODE == "local",
        #workers=os.cpu_count() * 2 + 1 if ENV_MODE != "local" else 3,
        proxy_headers=True if ENV_MODE == "local" else False,
    )
