# Kurulum ve ?al??t?rma K?lavuzu

## H?zl? Ba?lang??

### 1. Ba??ml?l?klar? Y?kleyin

```bash
# T?m ba??ml?l?klar? y?kleyin
npm run install:all
```

### 2. Backend Yap?land?rmas?

```bash
cd backend
cp .env.example .env
# .env dosyas?n? d?zenleyin (gerekirse)
```

### 3. Uygulamay? Ba?lat?n

```bash
# Root dizinde
npm run dev
```

Bu komut hem frontend (http://localhost:3000) hem de backend'i (http://localhost:3001) ba?lat?r.

## Geli?tirme Modu

### Frontend'i ayr? ?al??t?rma:
```bash
cd frontend
npm run dev
```

### Backend'i ayr? ?al??t?rma:
```bash
cd backend
npm run dev
```

## Production Build

```bash
# Frontend build
cd frontend
npm run build

# Build ??kt?s? frontend/dist/ klas?r?nde olacak
```

## Sorun Giderme

### Port zaten kullan?l?yor hatas?
- Frontend portu: `frontend/vite.config.ts` dosyas?nda de?i?tirilebilir
- Backend portu: `.env` dosyas?nda `PORT` de?i?keni ile de?i?tirilebilir

### CORS hatas?
- Backend'de CORS zaten yap?land?r?lm?? durumda
- Gerekirse `backend/server.js` dosyas?nda CORS ayarlar?n? d?zenleyin

### Mod?l bulunamad? hatas?
- `npm run install:all` komutunu tekrar ?al??t?r?n
- Her klas?rde `node_modules` klas?r?n?n varl???n? kontrol edin