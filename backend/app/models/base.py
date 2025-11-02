from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Float, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_premium = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    wardrobe_items = relationship("WardrobeItem", back_populates="owner")
    outfits = relationship("Outfit", back_populates="user")
    trips = relationship("Trip", back_populates="user")

class WardrobeItem(Base):
    __tablename__ = "wardrobe_items"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)  # ?st, alt, ayakkab?, aksesuar, d?? giyim
    subcategory = Column(String)  # g?mlek, pantolon, ti??rt, vb.
    color = Column(String)  # ana renk
    colors = Column(JSON)  # t?m renkler (?ok renkli k?yafetler i?in)
    brand = Column(String)
    image_url = Column(String, nullable=False)
    image_path = Column(String)  # S3 veya local path
    season = Column(String)  # ilkbahar, yaz, sonbahar, k??, hepsi
    occasion = Column(String)  # g?nl?k, i?, ak?am, spor, vb.
    style_tags = Column(JSON)  # klasik, spor, casual, formal, vb.
    purchase_date = Column(DateTime)
    last_worn = Column(DateTime)
    wear_count = Column(Integer, default=0)
    is_favorite = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    owner = relationship("User", back_populates="wardrobe_items")
    outfit_items = relationship("OutfitItem", back_populates="wardrobe_item")

class Outfit(Base):
    __tablename__ = "outfits"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String)
    occasion = Column(String)
    season = Column(String)
    style_score = Column(Float)  # AI'?n verdi?i stil uyum skoru
    is_saved = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="outfits")
    items = relationship("OutfitItem", back_populates="outfit", cascade="all, delete-orphan")

class OutfitItem(Base):
    __tablename__ = "outfit_items"
    
    id = Column(Integer, primary_key=True, index=True)
    outfit_id = Column(Integer, ForeignKey("outfits.id"), nullable=False)
    wardrobe_item_id = Column(Integer, ForeignKey("wardrobe_items.id"), nullable=False)
    position = Column(String)  # ?st, alt, ayakkab?, aksesuar, d?? giyim
    
    outfit = relationship("Outfit", back_populates="items")
    wardrobe_item = relationship("WardrobeItem", back_populates="outfit_items")

class ShoppingRecommendation(Base):
    __tablename__ = "shopping_recommendations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category = Column(String, nullable=False)
    reason = Column(Text)
    suggested_color = Column(String)
    suggested_style = Column(String)
    affiliate_link = Column(String)
    priority_score = Column(Float)  # ?ncelik skoru
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User")

class Trip(Base):
    __tablename__ = "trips"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    destination = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    duration_days = Column(Integer)
    occasion = Column(String)  # i?, tatil, resmi, vb.
    weather_forecast = Column(JSON)
    items = Column(JSON)  # seyahat i?in se?ilen k?yafetler
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="trips")
