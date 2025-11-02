from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.base import WardrobeItem, ShoppingRecommendation, User
from app.services.wardrobe_service import WardrobeService
from collections import Counter

class ShoppingService:
    def __init__(self, db: Session):
        self.db = db
        self.wardrobe_service = WardrobeService(db)
    
    def generate_recommendations(self, user_id: int) -> List[ShoppingRecommendation]:
        """
        Al??veri? ?nerileri olu?tur
        
        Gard?robun analizi yap?l?r ve eksik/eklenmesi gereken
        par?alar i?in ?neriler sunulur.
        """
        items = self.wardrobe_service.get_user_items(user_id)
        
        if len(items) < 5:
            # Yeni kullan?c?lar i?in temel ?neriler
            return self._get_basic_recommendations(user_id)
        
        recommendations = []
        
        # Kategori analizi
        category_counts = Counter(item.category for item in items)
        
        # En az bulunan kategoriler i?in ?neri
        min_category = min(category_counts.items(), key=lambda x: x[1])[0]
        recommendations.append(
            ShoppingRecommendation(
                user_id=user_id,
                category=min_category,
                reason=f"Gard?robunuzda {min_category} kategorisinde sadece {category_counts[min_category]} par?a var.",
                priority_score=0.8
            )
        )
        
        # Renk analizi
        color_counts = Counter(item.color for item in items if item.color)
        if len(color_counts) < 5:
            recommendations.append(
                ShoppingRecommendation(
                    user_id=user_id,
                    category="renk ?e?itlili?i",
                    reason="Gard?robunuzda renk ?e?itlili?i az. Farkl? renklerde par?alar ekleyin.",
                    priority_score=0.6
                )
            )
        
        # Stil ?e?itlili?i analizi
        occasion_counts = Counter(item.occasion for item in items if item.occasion)
        if "i?" not in occasion_counts:
            recommendations.append(
                ShoppingRecommendation(
                    user_id=user_id,
                    category="i? k?yafetleri",
                    reason="?? toplant?lar? i?in uygun k?yafetler ekleyin.",
                    priority_score=0.7
                )
            )
        
        self.db.add_all(recommendations)
        self.db.commit()
        
        return recommendations
    
    def _get_basic_recommendations(self, user_id: int) -> List[ShoppingRecommendation]:
        """Yeni kullan?c?lar i?in temel ?neriler"""
        basic_categories = [
            ("?st", "Temel ?st giyim par?alar? gard?robunuzun temelini olu?turur."),
            ("alt", "Pantolon ve etekler kombinasyonlar?n?z i?in gereklidir."),
            ("ayakkab?", "Ayakkab?lar kombinasyonlar?n?z? tamamlar."),
        ]
        
        recommendations = []
        for category, reason in basic_categories:
            recommendations.append(
                ShoppingRecommendation(
                    user_id=user_id,
                    category=category,
                    reason=reason,
                    priority_score=0.9
                )
            )
        
        self.db.add_all(recommendations)
        self.db.commit()
        
        return recommendations
    
    def get_category_recommendations(
        self,
        user_id: int,
        category: str
    ) -> List[ShoppingRecommendation]:
        """Belirli kategori i?in ?neriler"""
        return self.db.query(ShoppingRecommendation).filter(
            ShoppingRecommendation.user_id == user_id,
            ShoppingRecommendation.category == category
        ).order_by(ShoppingRecommendation.priority_score.desc()).all()
