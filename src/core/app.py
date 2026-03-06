# Emare Tedarik — Uygulama Fabrikası

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    """Uygulama fabrikası — FastAPI uygulamasını oluşturur."""
    app = FastAPI(
        title="Emare Tedarik",
        description="Tedarik zinciri yönetim sistemi",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Router'ları kaydet
    from src.api.v1.router import api_router
    app.include_router(api_router, prefix="/api/v1")

    @app.get("/health")
    async def health():
        return {"status": "ok", "app": "Emare Tedarik"}

    return app
