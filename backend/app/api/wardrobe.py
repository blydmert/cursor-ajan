from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models import schemas
from app.models.base import User, WardrobeItem
from app.services.wardrobe_service import WardrobeService
from app.services.image_service import ImageService

router = APIRouter()

# Ge?ici authentication - ger?ek uygulamada JWT token kullan?lmal?
def get_current_user(db: Session = Depends(get_db)):
    # ?imdilik ilk kullan?c?y? d?nd?r?yoruz
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/items", response_model=schemas.WardrobeItemResponse)
async def upload_item(
    file: UploadFile = File(...),
    name: str = None,
    category: str = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Yeni k?yafet foto?raf? y?kle"""
    service = WardrobeService(db)
    image_service = ImageService()
    
    # G?r?nt?y? y?kle ve analiz et
    image_data = await file.read()
    analysis = await image_service.analyze_clothing(image_data)
    
    # Veritaban?na kaydet
    item = await service.create_item(
        user_id=current_user.id,
        name=name or analysis.get("predicted_name", "Yeni K?yafet"),
        category=category or analysis.get("category", "di?er"),
        subcategory=analysis.get("subcategory"),
        color=analysis.get("dominant_color"),
        colors=analysis.get("colors"),
        image_data=image_data,
        image_filename=file.filename,
        metadata=analysis
    )
    
    return item

@router.get("/items", response_model=List[schemas.WardrobeItemResponse])
def get_items(
    category: str = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Kullan?c?n?n gard?rop ??elerini listele"""
    service = WardrobeService(db)
    items = service.get_user_items(user_id=current_user.id, category=category)
    return items

@router.get("/items/{item_id}", response_model=schemas.WardrobeItemResponse)
def get_item(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Belirli bir gard?rop ??esini getir"""
    service = WardrobeService(db)
    item = service.get_item(item_id=item_id, user_id=current_user.id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/items/{item_id}")
def delete_item(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Gard?rop ??esini sil"""
    service = WardrobeService(db)
    success = service.delete_item(item_id=item_id, user_id=current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}

@router.put("/items/{item_id}/favorite")
def toggle_favorite(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """??eyi favorilere ekle/??kar"""
    service = WardrobeService(db)
    item = service.toggle_favorite(item_id=item_id, user_id=current_user.id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"is_favorite": item.is_favorite}
