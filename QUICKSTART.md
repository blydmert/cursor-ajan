# ?? H?zl? Ba?lang?? Rehberi

AI M?zik Kompozisyon Asistan?'n? 5 dakikada ?al??t?r?n!

## ?n Gereksinimler

Sisteminizde a?a??dakilerin y?kl? oldu?undan emin olun:

- ? **Python 3.9+** ([?ndir](https://www.python.org/downloads/))
- ? **Node.js 16+** ([?ndir](https://nodejs.org/))
- ? **Git** ([?ndir](https://git-scm.com/))

Kurulumu kontrol edin:
```bash
python3 --version  # Python 3.9.0 veya ?zeri
node --version     # v16.0.0 veya ?zeri
npm --version      # 7.0.0 veya ?zeri
```

## Ad?m 1: Projeyi ?ndirin

```bash
git clone https://github.com/yourusername/ai-music-composer.git
cd ai-music-composer
```

## Ad?m 2: Otomatik Kurulum (?nerilen)

### Linux/Mac:
```bash
chmod +x start.sh
./start.sh
```

### Windows:
```bash
start.bat
```

Tebrikler! ?? Uygulama ?u adreslerde ?al???yor:
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Ad?m 3: Elle Kurulum (Alternatif)

### Backend Kurulumu

```bash
# 1. Backend dizinine git
cd backend

# 2. Sanal ortam olu?tur (?nerilir)
python3 -m venv venv

# 3. Sanal ortam? etkinle?tir
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Ba??ml?l?klar? y?kle
pip install -r requirements.txt

# 5. Sunucuyu ba?lat
python app.py
```

Backend ?imdi http://localhost:8000 adresinde ?al???yor! ?

### Frontend Kurulumu

Yeni bir terminal penceresi a??n:

```bash
# 1. Frontend dizinine git
cd frontend

# 2. Ba??ml?l?klar? y?kle
npm install

# 3. Development sunucusunu ba?lat
npm start
```

Frontend otomatik olarak http://localhost:3000 adresinde a??lacak! ?

## ?lk M?zi?inizi Olu?turun

1. Taray?c?da http://localhost:3000 adresine gidin
2. Anahtar kelimeler girin: "enerjik, elektronik, dans"
3. Parametreleri ayarlay?n (tempo, stil, anahtar)
4. "? M?zik Olu?tur" butonuna t?klay?n
5. M?zi?inizi dinleyin ve MIDI format?nda indirin!

## Docker ile ?al??t?rma (?ste?e Ba?l?)

Docker y?kl?yse:

```bash
docker-compose up
```

Hepsi bu kadar! ??

## Sorun Giderme

### Backend Ba?lam?yor

**Sorun**: `ModuleNotFoundError: No module named 'fastapi'`

**??z?m**:
```bash
cd backend
source venv/bin/activate  # veya venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

### Frontend Ba?lam?yor

**Sorun**: `Cannot find module 'react'`

**??z?m**:
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Port ?ak??mas?

**Sorun**: `Port 8000 already in use`

**??z?m**:
```bash
# Linux/Mac
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### CORS Hatalar?

**Sorun**: Frontend backend'e eri?emiyor

**??z?m**:
1. `backend/.env` dosyas?n? kontrol edin
2. `CORS_ORIGINS=http://localhost:3000` sat?r?n? ekleyin
3. Backend'i yeniden ba?lat?n

## Sonraki Ad?mlar

? Uygulamay? ke?fedin:
- Farkl? m?zik stilleri deneyin
- Tempo ve anahtar ayarlar?yla oynay?n
- MIDI dosyalar?n? DAW'?n?za import edin

?? Daha fazla bilgi i?in:
- [README.md](README.md) - T?m dok?mantasyon
- [API Docs](http://localhost:8000/docs) - API referans?
- [CONTRIBUTING.md](CONTRIBUTING.md) - Katk?da bulunma rehberi

?? Keyifli m?zik ?retimi!

## Destek

Sorun mu ya??yorsunuz?
- ?? [GitHub Issues](https://github.com/yourusername/ai-music-composer/issues)
- ?? Email: support@ai-music-composer.com
- ?? Discord: [Topluluk sunucusu](#)
