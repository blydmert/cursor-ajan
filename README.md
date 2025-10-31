# AI M?zik Kompozisyon Asistan? ??

?retken Yapay Zeka ile m?zisyenler, besteciler ve i?erik ?reticileri i?in ilham veren melodiler, armoni ilerleyi?leri ve ritimler ?reten yapay zeka arac?.

## ?? ?zellikler

- **Anahtar Kelime Tabanl? ?retim**: "enerjik, sinematik, elektronik" gibi kelimelerle m?zik olu?turun
- **?oklu Stil Deste?i**: Sinematik, elektronik, akustik, ambient, rock, jazz, klasik
- **?zelle?tirilebilir Parametreler**: S?re, tempo ve stil se?enekleri
- **Web Audio API Entegrasyonu**: Taray?c?da do?rudan ses ?alma
- **WAV ?ndirme**: Olu?turulan m?zikleri indirin
- **Modern UI/UX**: Kullan?c? dostu, responsive tasar?m

## ?? H?zl? Ba?lang??

### Gereksinimler

- Node.js 18+ 
- npm veya yarn

### Kurulum

1. T?m ba??ml?l?klar? y?kleyin:
```bash
npm run install:all
```

2. Geli?tirme modunda ?al??t?r?n:
```bash
npm run dev
```

Bu komut hem frontend'i (http://localhost:3000) hem de backend'i (http://localhost:3001) ba?lat?r.

### Ayr? ?al??t?rma

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**Backend:**
```bash
cd backend
npm install
npm run dev
```

## ?? Proje Yap?s?

```
ai-music-composition-assistant/
??? frontend/              # React + TypeScript frontend
?   ??? src/
?   ?   ??? components/   # React bile?enleri
?   ?   ??? services/     # API servisleri
?   ?   ??? App.tsx       # Ana uygulama
?   ??? package.json
??? backend/              # Node.js + Express backend
?   ??? routes/          # API route'lar?
?   ??? services/        # ?? mant??? servisleri
?   ??? server.js        # Ana sunucu dosyas?
??? package.json         # Root package.json
```

## ?? Kullan?m

1. Anahtar kelimelerinizi girin (?rn: "enerjik, sinematik, elektronik")
2. S?re, stil ve tempo parametrelerini se?in
3. "M?zik Olu?tur" butonuna t?klay?n
4. Olu?turulan m?zi?i dinleyin ve indirin

## ?? Teknolojiler

### Frontend
- **React 18** - UI framework
- **TypeScript** - Tip g?venli?i
- **Vite** - Build tool ve dev server
- **Web Audio API** - Ses ?alma ve i?leme
- **Axios** - HTTP istekleri
- **Lucide React** - ?konlar

### Backend
- **Node.js** - Runtime
- **Express** - Web framework
- **CORS** - Cross-origin deste?i

## ?? API Endpoints

### `POST /api/generate`
M?zik olu?turur.

**Request Body:**
```json
{
  "keywords": "enerjik, sinematik, elektronik",
  "duration": 120,
  "style": "cinematic",
  "tempo": "medium"
}
```

**Response:** WAV audio file (binary)

### `POST /api/convert-to-midi`
Audio dosyas?n? MIDI format?na d?n??t?r?r (yak?nda).

**Request Body:**
```json
{
  "audioUrl": "http://..."
}
```

### `GET /api/health`
Sa?l?k kontrol? endpoint'i.

## ?? Gelecek ?zellikler

- [ ] Ger?ek AI m?zik ?retimi entegrasyonu (MusicLM, MusicGen, vb.)
- [ ] MIDI export ?zelli?i
- [ ] Melodi m?r?ldanma ve tam orkestral d?zenleme
- [ ] Kullan?c? hesaplar? ve proje kaydetme
- [ ] Freemium model i?in abonelik sistemi
- [ ] Ses efektleri ve mixing ?zellikleri
- [ ] Topluluk payla??m ?zellikleri

## ?? Kullan?m Senaryolar?

### YouTube ??erik ?reticileri
Videolar?n?z i?in arka plan m?zi?i olu?turun. "enerjik, sinematik, elektronik" anahtar kelimeleriyle 2 dakikal?k ?zg?n m?zikler ?retin.

### Film ve Oyun Bestecileri
Farkl? sahneler i?in h?zl? prototipler olu?turun ve ilham al?n.

### Sosyal Medya ??erik ?reticileri
Instagram, TikTok ve di?er platformlar i?in ?zg?n m?zikler olu?turun.

## ?? Mevcut Durum

**Not:** ?u anda bu uygulama demo ama?l? basit sentetik ses ?retimi kullanmaktad?r. Ger?ek AI m?zik ?retimi i?in a?a??daki servislerden biri entegre edilmelidir:

- **Google MusicLM** - Text-to-music AI
- **Meta MusicGen** - Music generation model
- **OpenAI Music API** - OpenAI'nin m?zik API'si (bekleniyor)
- **Custom ML Models** - ?zel modeller

## ?? Lisans

MIT License

## ?? Katk?da Bulunma

Katk?lar?n?z? bekliyoruz! L?tfen issue a?arak veya pull request g?ndererek katk?da bulunun.

## ?? ?leti?im

Sorular?n?z i?in issue a?abilirsiniz.