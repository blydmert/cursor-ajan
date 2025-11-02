import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/wardrobe_db")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID", "")
    aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    aws_s3_bucket: str = os.getenv("AWS_S3_BUCKET", "wardrobe-uploads")
    jwt_secret: str = os.getenv("JWT_SECRET", "your-secret-key-change-in-production")
    ml_model_path: str = os.getenv("ML_MODEL_PATH", "./ml-models/clothing_classifier")
    
    class Config:
        env_file = ".env"

settings = Settings()

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
