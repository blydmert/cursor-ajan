# Ba?lang?? Rehberi

## H?zl? Ba?lang??

### 1. Backend Kurulumu

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Veritaban? Kurulumu

PostgreSQL'in kurulu oldu?undan emin olun:

```bash
# Docker ile
docker-compose up -d postgres

# Veya manuel olarak PostgreSQL olu?turun
createdb wardrobe_db
```

### 3. Environment Variables

`.env` dosyas? olu?turun:

```bash
cp backend/.env.example backend/.env
# .env dosyas?n? d?zenleyin ve ger?ek de?erleri girin
```

### 4. Veritaban? Migrasyonlar?

```bash
# Alembic ile (gelecekte)
alembic upgrade head

# Veya ?imdilik main.py ?al??t?r?ld???nda otomatik olu?turulur
```

### 5. Backend'i Ba?lat

```bash
cd backend
uvicorn app.main:app --reload
```

API dok?mantasyonu: http://localhost:8000/docs

### 6. Frontend Kurulumu (React Native)

```bash
cd frontend/mobile
npm install
```

iOS i?in:
```bash
cd ios && pod install && cd ..
npm run ios
```

Android i?in:
```bash
npm run android
```

## Docker ile ?al??t?rma

```bash
docker-compose up -d
```

Backend: http://localhost:8000

## Testler

```bash
cd backend
pytest tests/
```

## ?lk Kullan?c? Olu?turma

?u anda authentication basit bir placeholder. Ger?ek uygulamada:

1. Kay?t endpoint'i eklenmeli
2. JWT token authentication entegre edilmeli
3. Password hashing yap?lmal?

## Sonraki Ad?mlar

1. **ML Model Entegrasyonu**
   - TensorFlow/PyTorch modeli e?it
   - `backend/app/ml/` klas?r?ne entegre et
   - `image_service.py` i?inde kullan

2. **G?r?nt? Depolama**
   - AWS S3 veya Cloudinary hesab? olu?tur
   - `image_service.py` i?inde entegre et

3. **Authentication**
   - JWT token authentication ekle
   - User registration/login endpoints

4. **Frontend Geli?tirme**
   - React Native ekranlar? tamamla
   - API entegrasyonu yap

5. **Premium ?zellikler**
   - Payment gateway entegrasyonu
   - Premium limit kontrolleri

6. **Affiliate Links**
   - E-ticaret platformlar? ile entegrasyon
   - Commission tracking
