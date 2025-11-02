# AI Moda Stilisti ve Gard?rop Y?neticisi

Kullan?c?lar?n mevcut k?yafetlerinin foto?raflar?n? y?kleyerek kombin ?nerileri ald???, yeni al??veri?ler i?in tavsiyeler ald??? ve seyahatler i?in bavul haz?rlad??? bir uygulama.

## ?? De?er ?nerisi

- Mevcut gard?robu en verimli ?ekilde kullanma
- Stil sahibi olma
- Yanl?? al??veri?leri ?nleme

## ?? Hedef Kitle

Modaya ilgi duyan, zaman? k?s?tl? bireyler.

## ?? Gelir Modeli

- **Freemium Model**: Temel ?zellikler ?cretsiz, geli?mi? ?zellikler premium
- **Affiliate Komisyonlar?**: Al??veri? ?nerileri ?zerinden komisyon

## ??? Teknolojiler

### Backend
- FastAPI (Python)
- PostgreSQL
- Redis (caching)
- AWS S3 / Cloudinary (g?r?nt? depolama)
- TensorFlow / PyTorch (g?r?nt? tan?ma)

### Frontend
- React Native (iOS/Android)
- React (Web dashboard)

### AI/ML
- G?r?nt? s?n?fland?rma (k?yafet kategorileri)
- Renk analizi
- Stil uyumlulu?u algoritmas?
- ?neri sistemi

## ?? Proje Yap?s?

```
??? backend/              # Backend API
?   ??? app/
?   ?   ??? api/         # API endpoints
?   ?   ??? models/      # Veritaban? modelleri
?   ?   ??? services/    # ?? mant???
?   ?   ??? ml/          # ML modelleri ve servisleri
?   ?   ??? utils/       # Yard?mc? fonksiyonlar
?   ??? tests/           # Testler
?   ??? requirements.txt
??? frontend/            # Frontend uygulamas?
?   ??? mobile/         # React Native
?   ??? web/            # React web
??? ml-models/          # E?itilmi? ML modelleri
??? docs/               # Dok?mantasyon
??? docker-compose.yml  # Docker yap?land?rmas?
```

## ?? Kurulum

### Gereksinimler
- Python 3.9+
- Node.js 18+
- PostgreSQL 14+
- Docker (opsiyonel)

### Backend Kurulumu

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Environment Variables

`.env` dosyas? olu?turun:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/wardrobe_db
REDIS_URL=redis://localhost:6379
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_S3_BUCKET=wardrobe-uploads
JWT_SECRET=your_secret_key
ML_MODEL_PATH=./ml-models/clothing_classifier
```

### Frontend Kurulumu

```bash
cd frontend/mobile
npm install
# iOS
cd ios && pod install && cd ..
npm run ios
# Android
npm run android
```

## ?? ?zellikler

### Temel ?zellikler (?cretsiz)
- ? Gard?rop y?kleme (10 item'a kadar)
- ? Temel kombin ?nerileri
- ? K?yafet kategorilendirme

### Premium ?zellikler
- ?? S?n?rs?z gard?rop y?kleme
- ?? Geli?mi? AI kombin ?nerileri
- ?? Seyahat bavul haz?rlama
- ?? Al??veri? ?nerileri
- ?? AR sanal deneme (gelecek)

## ?? API Dok?mantasyonu

Backend ?al??t?ktan sonra: `http://localhost:8000/docs`

## ?? Testler

```bash
cd backend
pytest tests/
```

## ?? Lisans

MIT License
