# ML Model Integration

Bu klas?r e?itilmi? ML modellerini i?erir.

## Model Gereksinimleri

1. **K?yafet S?n?fland?rma Modeli**
   - Kategori tahmini (?st, alt, ayakkab?, vb.)
   - Alt kategori tahmini (g?mlek, pantolon, vb.)
   - Stil tahmini (klasik, spor, casual, vb.)

2. **Renk Analizi Modeli**
   - Dominant renk ??karma
   - ?ok renkli k?yafetler i?in renk paleti

3. **Stil Uyumlulu?u Modeli**
   - Kombinasyon skorlama
   - Renk uyumlulu?u

## Model Entegrasyonu

Modeller `backend/app/ml/` klas?r?nde entegre edilir ve
`backend/app/services/image_service.py` i?inde kullan?l?r.
