import uvicorn

from app.api import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "app.api:create_app", factory=True, host="0.0.0.0", port=5000, reload=True
    )
