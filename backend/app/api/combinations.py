from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.models import schemas
from app.models.base import User
from app.services.combination_service import CombinationService

router = APIRouter()

def get_current_user(db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/suggest", response_model=List[schemas.OutfitResponse])
def suggest_combinations(
    request: schemas.OutfitCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    limit: int = 3
):
    """
    Kombinasyon ?nerileri al
    
    ?rnek kullan?m:
    - Kullan?c? mavi ceket ve bej pantolon se?er
    - AI 3 farkl? kombin ?nerisi sunar
    """
    service = CombinationService(db)
    
    outfits = service.generate_combinations(
        user_id=current_user.id,
        occasion=request.occasion,
        season=request.season,
        preferred_items=request.preferred_items or [],
        limit=limit
    )
    
    return outfits

@router.get("/outfits", response_model=List[schemas.OutfitResponse])
def get_saved_outfits(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Kaydedilmi? kombinasyonlar? listele"""
    service = CombinationService(db)
    outfits = service.get_saved_outfits(user_id=current_user.id)
    return outfits

@router.post("/outfits/{outfit_id}/save")
def save_outfit(
    outfit_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Kombinasyonu kaydet"""
    service = CombinationService(db)
    outfit = service.save_outfit(outfit_id=outfit_id, user_id=current_user.id)
    if not outfit:
        raise HTTPException(status_code=404, detail="Outfit not found")
    return {"message": "Outfit saved successfully"}

@router.delete("/outfits/{outfit_id}")
def delete_outfit(
    outfit_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Kombinasyonu sil"""
    service = CombinationService(db)
    success = service.delete_outfit(outfit_id=outfit_id, user_id=current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Outfit not found")
    return {"message": "Outfit deleted successfully"}
