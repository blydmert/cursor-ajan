from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models import schemas
from app.models.base import User
from app.services.trip_service import TripService

router = APIRouter()

def get_current_user(db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/pack", response_model=schemas.TripResponse)
def create_trip_packing(
    request: schemas.TripCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Seyahat i?in bavul haz?rla
    
    AI, seyahat detaylar?na g?re gard?roptan
    uygun k?yafetleri se?er ve paketleme listesi olu?turur.
    """
    service = TripService(db)
    trip = service.create_trip_packing(
        user_id=current_user.id,
        name=request.name,
        destination=request.destination,
        start_date=request.start_date,
        end_date=request.end_date,
        occasion=request.occasion
    )
    return trip

@router.get("/trips", response_model=List[schemas.TripResponse])
def get_trips(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Kullan?c?n?n seyahatlerini listele"""
    service = TripService(db)
    trips = service.get_user_trips(user_id=current_user.id)
    return trips

@router.get("/trips/{trip_id}", response_model=schemas.TripResponse)
def get_trip(
    trip_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Belirli bir seyahat detaylar?n? getir"""
    service = TripService(db)
    trip = service.get_trip(trip_id=trip_id, user_id=current_user.id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip

@router.delete("/trips/{trip_id}")
def delete_trip(
    trip_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Seyahati sil"""
    service = TripService(db)
    success = service.delete_trip(trip_id=trip_id, user_id=current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {"message": "Trip deleted successfully"}
