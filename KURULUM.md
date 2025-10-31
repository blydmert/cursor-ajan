# ?? Ba??ml?l?klar? ?ndirme ve ?al??t?rma K?lavuzu

## Ad?m 1: Ba??ml?l?klar? ?ndirin

Proje klas?r?nde ?u komutu ?al??t?r?n:

```bash
npm run install:all
```

Bu komut:
- ? Root klas?r?ndeki ba??ml?l?klar? y?kler
- ? Frontend klas?r?ndeki ba??ml?l?klar? y?kler
- ? Backend klas?r?ndeki ba??ml?l?klar? y?kler

## Ad?m 2: Backend Yap?land?rmas? (Opsiyonel)

```bash
cd backend
cp .env.example .env
```

## Ad?m 3: Uygulamay? Ba?lat?n

```bash
# Root klas?r?nden
npm run dev
```

Bu komut hem frontend'i hem de backend'i ayn? anda ba?lat?r:
- ?? Frontend: http://localhost:3000
- ?? Backend API: http://localhost:3001

---

## Alternatif: Tek Tek ?al??t?rma

### Sadece Frontend:
```bash
cd frontend
npm install
npm run dev
```

### Sadece Backend:
```bash
cd backend
npm install
npm run dev
```

---

## ?? Sorun Giderme

### "npm: command not found" hatas?
Node.js y?kl? de?il. ?u komutla kontrol edin:
```bash
node --version
npm --version
```

### Port zaten kullan?l?yor
- Frontend portu de?i?tirmek i?in: `frontend/vite.config.ts`
- Backend portu de?i?tirmek i?in: `backend/.env` dosyas?nda `PORT=3001`

### Ba??ml?l?k hatalar?
```bash
# T?m node_modules klas?rlerini silin ve tekrar y?kleyin
rm -rf node_modules frontend/node_modules backend/node_modules
npm run install:all
```