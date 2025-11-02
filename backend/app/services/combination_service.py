from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.base import WardrobeItem, Outfit, OutfitItem, User
from app.services.styling_service import StylingService
import random

class CombinationService:
    def __init__(self, db: Session):
        self.db = db
        self.styling_service = StylingService()
    
    def generate_combinations(
        self,
        user_id: int,
        occasion: Optional[str] = None,
        season: Optional[str] = None,
        preferred_items: List[int] = [],
        limit: int = 3
    ) -> List[Outfit]:
        """
        Kombinasyon ?nerileri olu?tur
        
        ?rnek: Mavi ceket ve bej pantolon se?ildi?inde
        3 farkl? kombinasyon ?nerisi sunar.
        """
        # Kullan?c?n?n gard?robunu al
        all_items = self.db.query(WardrobeItem).filter(
            WardrobeItem.user_id == user_id
        ).all()
        
        if len(all_items) < 2:
            return []
        
        # Se?ilen ??eleri al
        selected_items = []
        if preferred_items:
            selected_items = [
                item for item in all_items if item.id in preferred_items
            ]
        
        # Kombinasyonlar olu?tur
        outfits = []
        for i in range(limit):
            outfit = self._create_outfit(
                user_id=user_id,
                all_items=all_items,
                selected_items=selected_items,
                occasion=occasion,
                season=season,
                index=i
            )
            outfits.append(outfit)
        
        return outfits
    
    def _create_outfit(
        self,
        user_id: int,
        all_items: List[WardrobeItem],
        selected_items: List[WardrobeItem],
        occasion: Optional[str],
        season: Optional[str],
        index: int
    ) -> Outfit:
        """Tek bir kombinasyon olu?tur"""
        outfit = Outfit(
            user_id=user_id,
            occasion=occasion,
            season=season,
            style_score=self.styling_service.calculate_style_score(selected_items)
        )
        self.db.add(outfit)
        self.db.flush()
        
        # Kombinasyon i?in ??eleri se?
        outfit_items = []
        
        # Se?ilen ??eleri ekle
        for item in selected_items:
            position = self._determine_position(item.category)
            outfit_item = OutfitItem(
                outfit_id=outfit.id,
                wardrobe_item_id=item.id,
                position=position
            )
            outfit_items.append(outfit_item)
        
        # Eksik kategoriler i?in ??eler se?
        used_categories = {item.category for item in selected_items}
        needed_categories = {"?st", "alt", "ayakkab?"}
        
        for category in needed_categories - used_categories:
            available_items = [
                item for item in all_items
                if item.category == category
                and item.id not in [oi.wardrobe_item_id for oi in outfit_items]
            ]
            
            if available_items:
                # Stil uyumuna g?re se?
                best_item = self.styling_service.select_compatible_item(
                    available_items, selected_items
                )
                if best_item:
                    position = self._determine_position(best_item.category)
                    outfit_item = OutfitItem(
                        outfit_id=outfit.id,
                        wardrobe_item_id=best_item.id,
                        position=position
                    )
                    outfit_items.append(outfit_item)
        
        # OutfitItem'lar? ekle
        for outfit_item in outfit_items:
            self.db.add(outfit_item)
        
        self.db.commit()
        self.db.refresh(outfit)
        
        return outfit
    
    def _determine_position(self, category: str) -> str:
        """Kategoriye g?re pozisyon belirle"""
        mapping = {
            "?st": "?st",
            "alt": "alt",
            "ayakkab?": "ayakkab?",
            "d?? giyim": "d?? giyim",
            "aksesuar": "aksesuar"
        }
        return mapping.get(category, "di?er")
    
    def get_saved_outfits(self, user_id: int) -> List[Outfit]:
        """Kaydedilmi? kombinasyonlar? getir"""
        return self.db.query(Outfit).filter(
            Outfit.user_id == user_id,
            Outfit.is_saved == True
        ).order_by(Outfit.created_at.desc()).all()
    
    def save_outfit(self, outfit_id: int, user_id: int) -> Optional[Outfit]:
        """Kombinasyonu kaydet"""
        outfit = self.db.query(Outfit).filter(
            Outfit.id == outfit_id,
            Outfit.user_id == user_id
        ).first()
        
        if outfit:
            outfit.is_saved = True
            self.db.commit()
            self.db.refresh(outfit)
            return outfit
        return None
    
    def delete_outfit(self, outfit_id: int, user_id: int) -> bool:
        """Kombinasyonu sil"""
        outfit = self.db.query(Outfit).filter(
            Outfit.id == outfit_id,
            Outfit.user_id == user_id
        ).first()
        
        if outfit:
            self.db.delete(outfit)
            self.db.commit()
            return True
        return False
