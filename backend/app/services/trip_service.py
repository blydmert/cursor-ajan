from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.base import Trip, WardrobeItem, User
from app.services.wardrobe_service import WardrobeService
from datetime import datetime, timedelta

class TripService:
    def __init__(self, db: Session):
        self.db = db
        self.wardrobe_service = WardrobeService(db)
    
    def create_trip_packing(
        self,
        user_id: int,
        name: str,
        destination: Optional[str],
        start_date: datetime,
        end_date: datetime,
        occasion: Optional[str]
    ) -> Trip:
        """
        Seyahat i?in bavul haz?rla
        
        AI, seyahat detaylar?na g?re gard?roptan
        uygun k?yafetleri se?er.
        """
        duration_days = (end_date - start_date).days + 1
        
        # Gard?roptan uygun ??eleri se?
        all_items = self.wardrobe_service.get_user_items(user_id)
        
        selected_items = self._select_items_for_trip(
            items=all_items,
            duration_days=duration_days,
            occasion=occasion
        )
        
        # Seyahat olu?tur
        trip = Trip(
            user_id=user_id,
            name=name,
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            duration_days=duration_days,
            occasion=occasion,
            items={
                "selected_items": [item.id for item in selected_items],
                "packing_list": self._create_packing_list(selected_items, duration_days)
            }
        )
        
        self.db.add(trip)
        self.db.commit()
        self.db.refresh(trip)
        
        return trip
    
    def _select_items_for_trip(
        self,
        items: List[WardrobeItem],
        duration_days: int,
        occasion: Optional[str]
    ) -> List[WardrobeItem]:
        """Seyahat i?in uygun ??eleri se?"""
        selected = []
        
        # Kategori baz?nda se?im
        categories = ["?st", "alt", "ayakkab?", "d?? giyim"]
        
        for category in categories:
            category_items = [item for item in items if item.category == category]
            
            if category_items:
                # Occasion'a g?re filtrele
                if occasion:
                    filtered = [
                        item for item in category_items
                        if item.occasion == occasion or item.occasion == "g?nl?k"
                    ]
                    if filtered:
                        category_items = filtered
                
                # ?e?itlilik i?in farkl? ??eler se?
                needed_count = min(2, duration_days // 3 + 1)
                selected.extend(category_items[:needed_count])
        
        return selected
    
    def _create_packing_list(
        self,
        items: List[WardrobeItem],
        duration_days: int
    ) -> dict:
        """Paketleme listesi olu?tur"""
        return {
            "tops": len([i for i in items if i.category == "?st"]),
            "bottoms": len([i for i in items if i.category == "alt"]),
            "shoes": len([i for i in items if i.category == "ayakkab?"]),
            "outerwear": len([i for i in items if i.category == "d?? giyim"]),
            "total_items": len(items)
        }
    
    def get_user_trips(self, user_id: int) -> List[Trip]:
        """Kullan?c?n?n seyahatlerini getir"""
        return self.db.query(Trip).filter(
            Trip.user_id == user_id
        ).order_by(Trip.start_date.desc()).all()
    
    def get_trip(self, trip_id: int, user_id: int) -> Optional[Trip]:
        """Belirli bir seyahat detaylar?n? getir"""
        return self.db.query(Trip).filter(
            Trip.id == trip_id,
            Trip.user_id == user_id
        ).first()
    
    def delete_trip(self, trip_id: int, user_id: int) -> bool:
        """Seyahati sil"""
        trip = self.get_trip(trip_id, user_id)
        if trip:
            self.db.delete(trip)
            self.db.commit()
            return True
        return False
