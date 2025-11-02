from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_premium: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# WardrobeItem Schemas
class WardrobeItemBase(BaseModel):
    name: str
    category: str
    subcategory: Optional[str] = None
    color: Optional[str] = None
    brand: Optional[str] = None
    season: Optional[str] = None
    occasion: Optional[str] = None

class WardrobeItemCreate(WardrobeItemBase):
    pass

class WardrobeItemResponse(WardrobeItemBase):
    id: int
    user_id: int
    image_url: str
    colors: Optional[dict] = None
    style_tags: Optional[List[str]] = None
    wear_count: int
    is_favorite: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Outfit Schemas
class OutfitItemResponse(BaseModel):
    wardrobe_item_id: int
    position: str
    wardrobe_item: WardrobeItemResponse
    
    class Config:
        from_attributes = True

class OutfitResponse(BaseModel):
    id: int
    user_id: int
    name: Optional[str] = None
    occasion: Optional[str] = None
    season: Optional[str] = None
    style_score: Optional[float] = None
    is_saved: bool
    items: List[OutfitItemResponse]
    created_at: datetime
    
    class Config:
        from_attributes = True

class OutfitCreate(BaseModel):
    occasion: Optional[str] = None
    season: Optional[str] = None
    preferred_items: Optional[List[int]] = None  # kullan?c?n?n belirtti?i item ID'leri

# Shopping Recommendation Schemas
class ShoppingRecommendationResponse(BaseModel):
    id: int
    category: str
    reason: Optional[str] = None
    suggested_color: Optional[str] = None
    suggested_style: Optional[str] = None
    affiliate_link: Optional[str] = None
    priority_score: float
    
    class Config:
        from_attributes = True

# Trip Schemas
class TripCreate(BaseModel):
    name: str
    destination: Optional[str] = None
    start_date: datetime
    end_date: datetime
    occasion: Optional[str] = None

class TripResponse(BaseModel):
    id: int
    user_id: int
    name: str
    destination: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    duration_days: Optional[int] = None
    occasion: Optional[str] = None
    items: Optional[dict] = None
    
    class Config:
        from_attributes = True
