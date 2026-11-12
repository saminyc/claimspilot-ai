
from fastapi import FastAPI

app = FastAPI(
    title="ClaimPilot AI API",
    description="Production-oriented AI insurance claims platform",
    version="0.1.0",
)


@app.get("/health", tags=["System"])
def health_check() -> dict[str, str]:
    return {"status": "healthy"}
