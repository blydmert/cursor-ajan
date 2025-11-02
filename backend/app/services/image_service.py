import os
import io
from typing import Dict, Optional
from PIL import Image
import numpy as np
from app.db.database import settings

class ImageService:
    """G?r?nt? analizi ve i?leme servisi"""
    
    def __init__(self):
        self.model_path = settings.ml_model_path
        
    async def analyze_clothing(self, image_data: bytes) -> Dict:
        """
        K?yafet g?r?nt?s?n? analiz eder
        
        Ger?ek uygulamada TensorFlow/PyTorch modeli kullan?lacak.
        ?imdilik temel analiz yap?yoruz.
        """
        try:
            image = Image.open(io.BytesIO(image_data))
            
            # Temel analiz
            analysis = {
                "category": self._predict_category(image),
                "subcategory": self._predict_subcategory(image),
                "dominant_color": self._extract_dominant_color(image),
                "colors": self._extract_colors(image),
                "predicted_name": self._generate_name(image)
            }
            
            return analysis
        except Exception as e:
            # Hata durumunda varsay?lan de?erler
            return {
                "category": "di?er",
                "subcategory": None,
                "dominant_color": None,
                "colors": {},
                "predicted_name": "Yeni K?yafet"
            }
    
    def _predict_category(self, image: Image.Image) -> str:
        """K?yafet kategorisini tahmin et (?st, alt, ayakkab?, vb.)"""
        # Ger?ek uygulamada ML modeli kullan?lacak
        # ?imdilik basit bir yakla??m
        width, height = image.size
        aspect_ratio = width / height
        
        if aspect_ratio > 1.2:
            return "?st"  # Geni? g?r?nt?ler genelde ?st giyim
        elif aspect_ratio < 0.8:
            return "alt"  # Uzun g?r?nt?ler genelde alt giyim
        else:
            return "di?er"
    
    def _predict_subcategory(self, image: Image.Image) -> Optional[str]:
        """Alt kategoriyi tahmin et (g?mlek, pantolon, vb.)"""
        # ML model entegrasyonu yap?lacak
        return None
    
    def _extract_dominant_color(self, image: Image.Image) -> Optional[str]:
        """Bask?n rengi ??kar"""
        try:
            # G?r?nt?y? k???lt (performans i?in)
            image = image.resize((150, 150))
            colors = image.getcolors(maxcolors=256*256*256)
            
            if not colors:
                return None
            
            # En ?ok g?r?nen rengi bul
            dominant_color = max(colors, key=lambda x: x[0])[1]
            
            # RGB'yi renk ismine ?evir
            return self._rgb_to_color_name(dominant_color)
        except:
            return None
    
    def _extract_colors(self, image: Image.Image) -> Dict:
        """T?m ?nemli renkleri ??kar"""
        return {
            "dominant": self._extract_dominant_color(image),
            "secondary": None  # ?kincil renk analizi eklenebilir
        }
    
    def _rgb_to_color_name(self, rgb: tuple) -> str:
        """RGB de?erini renk ismine ?evir"""
        if isinstance(rgb, (list, tuple)) and len(rgb) >= 3:
            r, g, b = rgb[0], rgb[1], rgb[2]
        else:
            return "di?er"
        
        # Basit renk kategorizasyonu
        if r > 200 and g > 200 and b > 200:
            return "beyaz"
        elif r < 50 and g < 50 and b < 50:
            return "siyah"
        elif r > g and r > b:
            if r > 150:
                return "k?rm?z?"
            return "k?rm?z?ms?"
        elif g > r and g > b:
            if g > 150:
                return "ye?il"
            return "ye?ilimsi"
        elif b > r and b > g:
            if b > 150:
                return "mavi"
            return "mavimsi"
        elif r > 150 and g > 150:
            return "sar?"
        elif r > 150 and g > 100 and b < 100:
            return "turuncu"
        elif r > 100 and g > 100 and b > 100:
            return "gri"
        elif r > 120 and g > 100 and b < 100:
            return "kahverengi"
        else:
            return "bej"
    
    def _generate_name(self, image: Image.Image) -> str:
        """K?yafet i?in otomatik isim olu?tur"""
        category = self._predict_category(image)
        color = self._extract_dominant_color(image)
        
        if color:
            return f"{color.capitalize()} {category}"
        return f"Yeni {category}"

    async def upload_to_storage(self, image_data: bytes, filename: str) -> str:
        """G?r?nt?y? bulut depolamaya y?kle"""
        # AWS S3 veya Cloudinary entegrasyonu
        # ?imdilik placeholder
        return f"https://storage.example.com/uploads/{filename}"
