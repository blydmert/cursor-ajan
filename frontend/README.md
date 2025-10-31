# AI Music Composer - Frontend

React tabanl? kullan?c? aray?z?.

## ?zellikler

- Modern ve kullan?c? dostu aray?z
- Ger?ek zamanl? m?zik ?alma (Web Audio API + Tone.js)
- MIDI export fonksiyonalitesi
- Responsive tasar?m
- Freemium model entegrasyonu

## Kurulum

```bash
# Ba??ml?l?klar? y?kle
npm install

# Geli?tirme sunucusunu ba?lat
npm start

# Production build
npm run build
```

## ?evre De?i?kenleri

`.env` dosyas? olu?turun:

```
REACT_APP_API_URL=http://localhost:8000
```

## Bile?enler

### MusicGenerator
M?zik olu?turma formu ve kontrolleri.

**Props:**
- `onGenerate(musicData)`: M?zik olu?turuldu?unda ?a?r?l?r
- `isPremium`: Premium ?zelliklerin etkin olup olmad???

### AudioPlayer
Web Audio API ile m?zik ?alma.

**Props:**
- `musicData`: Olu?turulan m?zik verisi
- `isPremium`: Premium ?zellikler i?in

**?zellikler:**
- Play/Pause kontrol?
- Progress bar
- Volume kontrol?
- MIDI export

### PricingModal
Fiyatland?rma planlar? modal'?.

**Props:**
- `onClose()`: Modal kapat?ld???nda
- `onUpgrade()`: Premium'a y?kseltildi?inde

## Geli?tirme

```bash
# Test ?al??t?r
npm test

# Linting
npm run lint

# Format
npm run format
```

## Tasar?m Sistemi

### Renkler
- Primary: `#667eea` (Mor-mavi)
- Secondary: `#764ba2` (Mor)
- Success: `#4caf50`
- Premium: `#ffd700` (Alt?n)

### Tipografi
- Font: System fonts (-apple-system, BlinkMacSystemFont, Segoe UI)
- Ba?l?klar: 2rem, 1.8rem, 1.5rem
- Body: 1rem

## Da??t?m

### Netlify/Vercel

```bash
npm run build
# Deploy build/ dizinini
```

### S3 + CloudFront

```bash
npm run build
aws s3 sync build/ s3://your-bucket/
```

## Performans

- Lazy loading bile?enleri
- Code splitting
- Tone.js optimizasyonu
- Memoization kullan?m?
