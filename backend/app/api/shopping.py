from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models import schemas
from app.models.base import User
from app.services.shopping_service import ShoppingService

router = APIRouter()

def get_current_user(db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/recommendations", response_model=List[schemas.ShoppingRecommendationResponse])
def get_shopping_recommendations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Al??veri? ?nerileri al
    
    AI gard?robunu analiz eder ve eksik/eklenmesi gereken
    par?alar i?in ?neriler sunar.
    """
    service = ShoppingService(db)
    recommendations = service.generate_recommendations(user_id=current_user.id)
    return recommendations

@router.get("/recommendations/{category}")
def get_category_recommendations(
    category: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Belirli bir kategori i?in al??veri? ?nerileri"""
    service = ShoppingService(db)
    recommendations = service.get_category_recommendations(
        user_id=current_user.id,
        category=category
    )
    return recommendations
