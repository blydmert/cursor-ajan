from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import wardrobe, combinations, shopping, trips
from app.db.database import engine, Base

# Veritaban? tablolar?n? olu?tur
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Moda Stilisti API",
    description="Gard?rop y?netimi ve kombin ?nerileri i?in AI destekli API",
    version="1.0.0"
)

# CORS ayarlar?
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production'da spesifik domainler belirtilmeli
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API rotalar?
app.include_router(wardrobe.router, prefix="/api/wardrobe", tags=["Gard?rop"])
app.include_router(combinations.router, prefix="/api/combinations", tags=["Kombinasyonlar"])
app.include_router(shopping.router, prefix="/api/shopping", tags=["Al??veri?"])
app.include_router(trips.router, prefix="/api/trips", tags=["Seyahatler"])

@app.get("/")
async def root():
    return {
        "message": "AI Moda Stilisti API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
