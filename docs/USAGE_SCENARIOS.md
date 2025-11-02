# Kullan?m Senaryolar?

## Senaryo 1: ?? Toplant?s? i?in Kombinasyon ?nerisi

**Kullan?c? Hikayesi:**
Kullan?c? ?nemli bir i? toplant?s? i?in dolab?ndaki mavi ceket ve bej pantolonu kullanarak ne giyebilece?ine dair 3 farkl? kombin ?nerisi al?r.

**API Kullan?m?:**

```bash
POST /api/combinations/suggest
{
  "occasion": "i?",
  "preferred_items": [123, 456]  # Mavi ceket ve bej pantolon ID'leri
}

# Response: 3 farkl? kombinasyon ?nerisi
```

**Sonu?:**
- Kombinasyon 1: Mavi ceket + Bej pantolon + Siyah ayakkab? + Beyaz g?mlek
- Kombinasyon 2: Mavi ceket + Bej pantolon + Kahverengi ayakkab? + Mavi g?mlek
- Kombinasyon 3: Mavi ceket + Bej pantolon + Siyah ayakkab? + Gri kazak

## Senaryo 2: Yeni K?yafet Y?kleme

**Kullan?c? Hikayesi:**
Kullan?c? yeni ald??? bir g?mle?in foto?raf?n? ?eker ve uygulamaya y?kler.

**API Kullan?m?:**

```bash
POST /api/wardrobe/items
Content-Type: multipart/form-data
- file: [g?mlek foto?raf?]
- name: "Mavi G?mlek"
- category: "?st"
```

**AI Analizi:**
- Kategori: ?st
- Alt kategori: G?mlek
- Renk: Mavi
- Stil: Klasik
- Occasion: ??, G?nl?k

## Senaryo 3: Seyahat Bavul Haz?rlama

**Kullan?c? Hikayesi:**
Kullan?c? 5 g?nl?k bir i? seyahati i?in bavul haz?rlamak istiyor.

**API Kullan?m?:**

```bash
POST /api/trips/pack
{
  "name": "?stanbul ?? Seyahati",
  "destination": "?stanbul",
  "start_date": "2024-01-15T00:00:00",
  "end_date": "2024-01-19T23:59:59",
  "occasion": "i?"
}
```

**Sonu?:**
- 3 ?st giyim
- 2 alt giyim
- 2 ayakkab?
- 1 d?? giyim
- Detayl? paketleme listesi

## Senaryo 4: Al??veri? ?nerileri

**Kullan?c? Hikayesi:**
Kullan?c? gard?robunda eksik olan par?alar? ??renmek istiyor.

**API Kullan?m?:**

```bash
GET /api/shopping/recommendations
```

**Sonu?:**
- ?neri 1: Ayakkab? kategorisinde sadece 2 par?a var, ?e?itlilik i?in ?nerilir
- ?neri 2: Renk ?e?itlili?i az, farkl? renklerde par?alar eklenebilir
- ?neri 3: ?? k?yafetleri eksik, i? toplant?lar? i?in uygun k?yafetler ?nerilir
