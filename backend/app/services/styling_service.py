from typing import List, Optional
from app.models.base import WardrobeItem

class StylingService:
    """Stil uyumlulu?u ve kombinasyon algoritmalar?"""
    
    # Renk uyumluluk kurallar?
    COLOR_COMPATIBILITY = {
        "siyah": ["beyaz", "gri", "k?rm?z?", "mavi", "ye?il", "bej"],
        "beyaz": ["siyah", "gri", "mavi", "k?rm?z?", "ye?il", "bej"],
        "mavi": ["beyaz", "siyah", "bej", "gri", "kahverengi"],
        "bej": ["mavi", "siyah", "beyaz", "kahverengi", "gri"],
        "kahverengi": ["bej", "beyaz", "mavi", "ye?il"],
        "gri": ["siyah", "beyaz", "mavi", "k?rm?z?"],
        "k?rm?z?": ["siyah", "beyaz", "gri", "mavi"],
    }
    
    def calculate_style_score(self, items: List[WardrobeItem]) -> float:
        """
        Kombinasyonun stil skorunu hesapla
        
        0.0 - 1.0 aras? de?er d?ner
        """
        if len(items) < 2:
            return 0.5
        
        scores = []
        
        # Renk uyumlulu?u kontrol?
        color_score = self._check_color_compatibility(items)
        scores.append(color_score)
        
        # Stil uyumlulu?u kontrol?
        style_score = self._check_style_compatibility(items)
        scores.append(style_score)
        
        # Occasion uyumlulu?u
        occasion_score = self._check_occasion_compatibility(items)
        scores.append(occasion_score)
        
        # Ortalama skor
        return sum(scores) / len(scores)
    
    def _check_color_compatibility(self, items: List[WardrobeItem]) -> float:
        """Renk uyumlulu?unu kontrol et"""
        colors = [item.color for item in items if item.color]
        
        if len(colors) < 2:
            return 0.7
        
        # Temel renklerin uyumunu kontrol et
        for i in range(len(colors) - 1):
            color1 = colors[i]
            color2 = colors[i + 1]
            
            if color1 in self.COLOR_COMPATIBILITY:
                if color2 in self.COLOR_COMPATIBILITY[color1]:
                    return 0.9
            
            # Ayn? renk tonlar? da uyumlu say?l?r
            if color1 == color2:
                return 0.8
        
        return 0.6
    
    def _check_style_compatibility(self, items: List[WardrobeItem]) -> float:
        """Stil uyumlulu?unu kontrol et"""
        style_tags = []
        for item in items:
            if item.style_tags:
                style_tags.extend(item.style_tags)
        
        if not style_tags:
            return 0.7
        
        # Ayn? stil etiketleri varsa daha uyumlu
        unique_tags = set(style_tags)
        if len(unique_tags) <= len(style_tags) / 2:
            return 0.9
        
        return 0.7
    
    def _check_occasion_compatibility(self, items: List[WardrobeItem]) -> float:
        """Occasion uyumlulu?unu kontrol et"""
        occasions = [item.occasion for item in items if item.occasion]
        
        if not occasions:
            return 0.7
        
        # T?m ??eler ayn? occasion'a sahipse
        if len(set(occasions)) == 1:
            return 0.95
        
        # "G?nl?k" her ?eyle uyumlu
        if "g?nl?k" in occasions:
            return 0.8
        
        return 0.6
    
    def select_compatible_item(
        self,
        available_items: List[WardrobeItem],
        selected_items: List[WardrobeItem]
    ) -> Optional[WardrobeItem]:
        """Mevcut ??elerle uyumlu bir ??e se?"""
        if not available_items:
            return None
        
        if not selected_items:
            return available_items[0]
        
        # Her ??e i?in uyum skoru hesapla
        best_item = None
        best_score = 0.0
        
        for item in available_items:
            test_items = selected_items + [item]
            score = self.calculate_style_score(test_items)
            
            if score > best_score:
                best_score = score
                best_item = item
        
        return best_item or available_items[0]
