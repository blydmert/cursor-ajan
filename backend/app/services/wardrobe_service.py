from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.base import WardrobeItem, User
from app.services.image_service import ImageService
from app.db.database import settings
import boto3
from datetime import datetime

class WardrobeService:
    def __init__(self, db: Session):
        self.db = db
        self.image_service = ImageService()
        
    async def create_item(
        self,
        user_id: int,
        name: str,
        category: str,
        subcategory: Optional[str] = None,
        color: Optional[str] = None,
        colors: Optional[dict] = None,
        image_data: bytes = None,
        image_filename: str = None,
        metadata: Optional[dict] = None
    ) -> WardrobeItem:
        """Yeni gard?rop ??esi olu?tur"""
        
        # Kullan?c?n?n premium olup olmad???n? kontrol et
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")
        
        # ?cretsiz kullan?c?lar i?in limit kontrol?
        if not user.is_premium:
            item_count = self.db.query(WardrobeItem).filter(
                WardrobeItem.user_id == user_id
            ).count()
            if item_count >= 10:
                raise ValueError("Free users can only upload 10 items. Upgrade to premium!")
        
        # G?r?nt?y? y?kle
        image_url = await self.image_service.upload_to_storage(
            image_data, image_filename or "item.jpg"
        )
        
        # Veritaban?na kaydet
        item = WardrobeItem(
            user_id=user_id,
            name=name,
            category=category,
            subcategory=subcategory,
            color=color,
            colors=colors or {},
            image_url=image_url,
            image_path=image_filename,
            style_tags=metadata.get("style_tags") if metadata else None
        )
        
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        
        return item
    
    def get_user_items(self, user_id: int, category: Optional[str] = None) -> List[WardrobeItem]:
        """Kullan?c?n?n gard?rop ??elerini getir"""
        query = self.db.query(WardrobeItem).filter(WardrobeItem.user_id == user_id)
        
        if category:
            query = query.filter(WardrobeItem.category == category)
        
        return query.order_by(WardrobeItem.created_at.desc()).all()
    
    def get_item(self, item_id: int, user_id: int) -> Optional[WardrobeItem]:
        """Belirli bir ??eyi getir"""
        return self.db.query(WardrobeItem).filter(
            WardrobeItem.id == item_id,
            WardrobeItem.user_id == user_id
        ).first()
    
    def delete_item(self, item_id: int, user_id: int) -> bool:
        """??eyi sil"""
        item = self.get_item(item_id, user_id)
        if item:
            self.db.delete(item)
            self.db.commit()
            return True
        return False
    
    def toggle_favorite(self, item_id: int, user_id: int) -> Optional[WardrobeItem]:
        """Favori durumunu de?i?tir"""
        item = self.get_item(item_id, user_id)
        if item:
            item.is_favorite = not item.is_favorite
            self.db.commit()
            self.db.refresh(item)
            return item
        return None
