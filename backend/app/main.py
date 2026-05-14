from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.stocks import router as stocks_router


app = FastAPI(title="vibe_test backend")

# Permissive CORS is fine here because this starter is for local development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stocks_router, prefix="/api/stocks", tags=["stocks"])


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Welcome to the vibe_test backend",
        "docs": "/docs",
    }
