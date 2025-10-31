# ?? AI M?zik Kompozisyon Asistan?

M?zisyenler, besteciler ve i?erik ?reticileri i?in ilham veren melodiler, armoni ilerleyi?leri ve ritimler ?reten yapay zeka destekli m?zik kompozisyon arac?.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![React](https://img.shields.io/badge/react-18.2-blue.svg)

## ?? ?zellikler

### Temel ?zellikler (?cretsiz)
- ?? **AI Destekli Kompozisyon**: Anahtar kelimelerden m?zik olu?turma
- ?? **?oklu Enstr?man Deste?i**: Melodi, armoni ve bas hatlar?
- ?? **M?zik Teorisi**: Do?ru akord ilerleyi?leri ve skala kullan?m?
- ??? **?zelle?tirilebilir Parametreler**: Tempo, anahtar, skala se?imi
- ?? **MIDI Export**: Olu?turulan m?zi?i MIDI format?nda indirme
- ?? **Ger?ek Zamanl? Playback**: Web Audio API ile taray?c?da ?alma

### Premium ?zellikler
- ? **Uzun S?reli M?zikler**: 5 dakikaya kadar kompozisyon
- ?? **Davul Partileri**: Profesyonel ritim b?l?mleri
- ?? **Ek Melodiler**: ?ok katmanl? d?zenlemeler
- ?? **Y?ksek Kalite Export**: WAV ve MP3 formatlar? (320kbps)
- ?? **S?n?rs?z Olu?turma**: G?nl?k limit yok
- ?? **Ticari Kullan?m**: Telif hakk? endi?esi olmadan kullan?m

## ?? De?er ?nerisi

- ? Yarat?c? blokaj? a?maya yard?mc? olma
- ? Kompozisyon s?recini h?zland?rma
- ?? Telifsiz ?zg?n m?zikler olu?turma
- ?? ?lham verici m?zikal fikirler

## ?? Hedef Kitle

- ?? **M?zisyenler**: ?lham ve yeni fikirler arayan sanat??lar
- ?? **Film/Oyun Bestecileri**: H?zl? prototip ihtiyac? olanlar
- ?? **??erik ?reticileri**: YouTube, TikTok, Instagram i?in ?zg?n m?zik arayanlar
- ?? **M?zik ??rencileri**: Kompozisyon tekniklerini ??renenler

## ?? Kurulum

### Gereksinimler

- Python 3.9+
- Node.js 16+
- npm veya yarn

### Backend Kurulumu

```bash
# Backend dizinine gidin
cd backend

# Sanal ortam olu?turun (?nerilir)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Ba??ml?l?klar? y?kleyin
pip install -r requirements.txt

# Sunucuyu ba?lat?n
python app.py
```

Backend sunucusu `http://localhost:8000` adresinde ?al??acakt?r.

### Frontend Kurulumu

```bash
# Frontend dizinine gidin
cd frontend

# Ba??ml?l?klar? y?kleyin
npm install

# Geli?tirme sunucusunu ba?lat?n
npm start
```

Frontend uygulamas? `http://localhost:3000` adresinde a??lacakt?r.

## ?? Kullan?m

### Temel Kullan?m

1. **Anahtar Kelime Giri?i**: M?zi?inizin karakterini tan?mlayan kelimeler girin
   - ?rnek: "enerjik, sinematik, elektronik"
   - ?rnek: "sakin, ambient, piyano"

2. **Parametreleri Ayarlay?n**:
   - M?zik stili se?in (Electronic, Cinematic, Jazz, vb.)
   - S?re belirleyin (?cretsiz: 30 saniye, premium: 5 dakika)
   - Tempo (BPM) ayarlay?n
   - M?zikal anahtar ve skala se?in

3. **Olu?tur**: "M?zik Olu?tur" butonuna t?klay?n

4. **Dinleyin ve ?ndirin**: 
   - Olu?turulan m?zi?i hemen dinleyin
   - MIDI format?nda indirin
   - Premium: WAV/MP3 formatlar?nda indirin

### ?rnek Kullan?m Senaryolar?

#### YouTube ??erik ?reticisi
```
Anahtar Kelimeler: enerjik, sinematik, elektronik
Stil: Cinematic
S?re: 2 dakika (120 saniye)
Tempo: 140 BPM
Sonu?: Video arka plan? i?in 2 dakikal?k ?zg?n m?zik
```

#### Meditasyon Uygulamas?
```
Anahtar Kelimeler: sakin, ambient, meditasyon
Stil: Ambient
S?re: 5 dakika (Premium)
Tempo: 60 BPM
Sonu?: Gev?eme seanslar? i?in uzun s?reli m?zik
```

#### Ba??ms?z Oyun Geli?tiricisi
```
Anahtar Kelimeler: karanl?k, gizemli, epik
Stil: Cinematic
S?re: 3 dakika
Tempo: 80 BPM
Sonu?: Oyun men?s? i?in atmosferik m?zik
```

## ??? Teknoloji Y???n?

### Backend
- **FastAPI**: Modern, h?zl? Python web framework
- **Python**: M?zik ?retim algoritmalar?
- **Mido**: MIDI dosya i?leme
- **Music Theory Libraries**: Akord ilerleyi?leri ve skala mant???

### Frontend
- **React**: Kullan?c? aray?z?
- **Tone.js**: Web Audio API ile ses sentezi
- **@tonejs/midi**: MIDI dosya olu?turma ve export
- **Axios**: API ileti?imi

### Altyap?
- Web Audio API
- MIDI Protocol
- RESTful API

## ?? ?? Modeli

### Freemium Model

| ?zellik | ?cretsiz | Premium (?99/ay) |
|---------|----------|------------------|
| Maksimum S?re | 30 saniye | 5 dakika |
| Enstr?manlar | Temel | T?m + Davul |
| Export Formatlar? | MIDI | MIDI, WAV, MP3 |
| G?nl?k Limit | 5 olu?turma | S?n?rs?z |
| Kalite | Standart | Y?ksek (320kbps) |
| Ticari Kullan?m | ? | ? |
| ?ncelikli Destek | ? | ? |

### Gelir Ak??lar?

1. **Ayl?k Abonelik**: Premium ?zellikler i?in ?99/ay
2. **Y?ll?k Abonelik**: ?990/y?l (%17 indirim)
3. **Kurumsal Paket**: Tak?mlar i?in ?zel fiyatland?rma
4. **API Eri?imi**: Geli?tiriciler i?in API kredileri

## ?? Zorluklar ve Riskler

### Teknik Zorluklar
- ? **M?zikal Kalite**: Algoritmik kompozisyon ile 'insans?' sonu?lar
- ? **Performans**: Ger?ek zamanl? m?zik ?retimi optimizasyonu
- ?? **?l?eklenebilirlik**: Y?ksek kullan?c? trafi?i y?netimi

### ?? Riskleri
- **Telif Hakk?**: Olu?turulan m?ziklerin ?zg?nl??? garanti edilmeli
- **Rekabet**: Benzer AI m?zik ara?lar? (Amper, AIVA, Soundful)
- **Kullan?c? Beklentileri**: Kalite ve ?e?itlilik beklentileri

### ??z?mler
- Benzersiz algoritma ve m?zik teorisi kombinasyonu
- ?zg?nl?k kontrol? mekanizmalar?
- S?rekli model iyile?tirme
- Kullan?c? geri bildirimi ile ??renme

## ?? Gelecek ?zellikleri

### Yak?n Gelecek (3-6 ay)
- [ ] M?r?ldanma/mikrofon giri?i ile melodi yakalama
- [ ] Stem export (ayr? enstr?man dosyalar?)
- [ ] Daha fazla m?zik stili (Hip-Hop, R&B, Country)
- [ ] Kullan?c? profilleri ve kaydetme
- [ ] ??birli?i ?zellikleri

### Uzun Vadeli (6-12 ay)
- [ ] **Orkestral D?zenleme**: M?r?ldanan melodiyi tam orkestra d?zenlemesine d?n??t?rme
- [ ] AI Vokal Sentezi
- [ ] Video ile senkronizasyon
- [ ] Mobil uygulamalar (iOS/Android)
- [ ] DAW Eklentileri (VST/AU)
- [ ] ?zel model e?itimi

## ?? API Dok?mantasyonu

### Endpoints

#### `POST /generate`
Anahtar kelimelerden m?zik olu?turur.

**Request Body:**
```json
{
  "keywords": ["energetic", "cinematic"],
  "duration": 60,
  "style": "electronic",
  "tempo": 120,
  "key": "C",
  "scale": "major",
  "is_premium": false
}
```

**Response:**
```json
{
  "id": "uuid",
  "midi_data": {
    "tempo": 120,
    "tracks": { ... }
  },
  "metadata": { ... }
}
```

#### `GET /styles`
Kullan?labilir m?zik stillerini listeler.

#### `GET /health`
Sunucu durumunu kontrol eder.

## ?? Katk?da Bulunma

Katk?lar?n?z? bekliyoruz! L?tfen ?u ad?mlar? izleyin:

1. Fork edin
2. Feature branch olu?turun (`git checkout -b feature/AmazingFeature`)
3. De?i?ikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request a??n

## ?? Lisans

Bu proje MIT lisans? alt?nda lisanslanm??t?r. Detaylar i?in `LICENSE` dosyas?na bak?n.

## ?? ?leti?im

- Website: [ai-music-composer.com](https://ai-music-composer.com)
- Email: support@ai-music-composer.com
- Twitter: [@AIMusicComposer](https://twitter.com/AIMusicComposer)

## ?? Te?ekk?rler

- Tone.js toplulu?una ses sentezi i?in
- FastAPI geli?tiricilerine harika framework i?in
- A??k kaynak m?zik k?t?phanesi katk?da bulunanlara

---

**Not**: Bu bir AI destekli m?zik olu?turma arac?d?r. Olu?turulan m?zikler algoritmik olarak ?retilir ve telif hakk?ndan muaft?r, ancak profesyonel kullan?m i?in her zaman kontrol edilmelidir.

? Projeyi be?endiyseniz, y?ld?z vermeyi unutmay?n!
