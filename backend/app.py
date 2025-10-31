from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import random
import json
from music_generator import MusicGenerator

app = FastAPI(title="AI Music Composition Assistant")

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

music_gen = MusicGenerator()

class GenerationRequest(BaseModel):
    keywords: List[str]
    duration: int = 30  # seconds
    style: Optional[str] = "electronic"
    tempo: Optional[int] = 120
    key: Optional[str] = "C"
    scale: Optional[str] = "major"
    is_premium: Optional[bool] = False

class GenerationResponse(BaseModel):
    id: str
    midi_data: dict
    audio_url: Optional[str] = None
    metadata: dict

@app.get("/")
async def root():
    return {
        "message": "AI Music Composition Assistant API",
        "version": "1.0.0",
        "endpoints": [
            "/generate - Generate music from keywords",
            "/styles - Get available music styles",
            "/export - Export generated music"
        ]
    }

@app.post("/generate", response_model=GenerationResponse)
async def generate_music(request: GenerationRequest):
    """
    Generate music based on keywords and parameters
    """
    try:
        # Generate music composition
        composition = music_gen.generate(
            keywords=request.keywords,
            duration=request.duration,
            style=request.style,
            tempo=request.tempo,
            key=request.key,
            scale=request.scale,
            is_premium=request.is_premium
        )
        
        return GenerationResponse(
            id=composition["id"],
            midi_data=composition["midi_data"],
            audio_url=composition.get("audio_url"),
            metadata=composition["metadata"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/styles")
async def get_styles():
    """
    Get available music styles
    """
    return {
        "styles": [
            {"id": "electronic", "name": "Electronic", "description": "Modern electronic music"},
            {"id": "cinematic", "name": "Cinematic", "description": "Epic film scores"},
            {"id": "ambient", "name": "Ambient", "description": "Atmospheric soundscapes"},
            {"id": "jazz", "name": "Jazz", "description": "Jazz progressions"},
            {"id": "classical", "name": "Classical", "description": "Classical compositions"},
            {"id": "rock", "name": "Rock", "description": "Rock and pop"},
            {"id": "lofi", "name": "Lo-Fi", "description": "Relaxed lo-fi beats"}
        ]
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
