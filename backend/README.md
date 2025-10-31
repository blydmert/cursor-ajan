# AI Music Composer - Backend

FastAPI tabanl? m?zik ?retim API'si.

## ?zellikler

- **Algoritmik Kompozisyon**: M?zik teorisi kurallar?na dayal? m?zik ?retimi
- **?oklu M?zik Stilleri**: Electronic, Cinematic, Jazz, Classical, vb.
- **MIDI ?retimi**: Standart MIDI format?nda export
- **?zelle?tirilebilir Parametreler**: Tempo, anahtar, skala, s?re

## Kurulum

```bash
# Sanal ortam olu?tur
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Ba??ml?l?klar? y?kle
pip install -r requirements.txt

# Sunucuyu ba?lat
python app.py
```

Sunucu http://localhost:8000 adresinde ?al??acakt?r.

## API Dok?mantasyonu

Sunucu ?al???rken http://localhost:8000/docs adresinden Swagger UI'ye eri?ebilirsiniz.

## Geli?tirme

```bash
# Test mod ile ?al??t?r
uvicorn app:app --reload

# Formatlamak i?in
black .

# Linting i?in
flake8 .
```

## Mimari

### MusicGenerator S?n?f?

Ana m?zik ?retim motoru:

- **Skala Sistemleri**: Major, minor, pentatonic, blues, dorian, phrygian
- **Akord ?lerleyi?leri**: Pop, emotional, dark, uplifting, jazzy
- **Ritim Desenleri**: Energetic, relaxed, syncopated, steady

### Algoritma

1. Anahtar kelimeleri analiz et (enerji, karma??kl?k, karanl?k seviyesi)
2. Uygun skala ve akord ilerleyi?i se?
3. Melodi hatt? ?ret (skala notlar?n? kullanarak)
4. Armoni ?ret (akord ilerleyi?inden)
5. Bas hatt? ?ret (akord k?klerinden)
6. Davul deseni ekle (premium)
7. MIDI format?nda derle

## Yap?land?rma

?evre de?i?kenleri (.env):

```
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:3000
```

## Da??t?m

### Docker ile

```bash
docker build -t ai-music-backend .
docker run -p 8000:8000 ai-music-backend
```

### Geleneksel Sunucu

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
```
