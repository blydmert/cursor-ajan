# AI Moda Stilisti - Dok?mantasyon

## Genel Bak??

AI Moda Stilisti, kullan?c?lar?n gard?roplar?n? y?netmelerine ve AI destekli kombinasyon ?nerileri almalar?na yard?mc? olan bir uygulamad?r.

## Mimari

### Backend
- **FastAPI**: RESTful API
- **PostgreSQL**: Veritaban?
- **Redis**: Cache ve oturum y?netimi
- **AWS S3**: G?r?nt? depolama
- **TensorFlow/PyTorch**: ML modelleri

### Frontend
- **React Native**: iOS ve Android mobil uygulama
- **React**: Web dashboard

## API Endpoints

### Gard?rop Y?netimi
- `POST /api/wardrobe/items` - Yeni k?yafet y?kle
- `GET /api/wardrobe/items` - Gard?rop listesi
- `GET /api/wardrobe/items/{id}` - ??e detay?
- `DELETE /api/wardrobe/items/{id}` - ??e sil
- `PUT /api/wardrobe/items/{id}/favorite` - Favori durumu de?i?tir

### Kombinasyonlar
- `POST /api/combinations/suggest` - Kombinasyon ?nerileri al
- `GET /api/combinations/outfits` - Kaydedilmi? kombinasyonlar
- `POST /api/combinations/outfits/{id}/save` - Kombinasyon kaydet
- `DELETE /api/combinations/outfits/{id}` - Kombinasyon sil

### Al??veri?
- `GET /api/shopping/recommendations` - Al??veri? ?nerileri
- `GET /api/shopping/recommendations/{category}` - Kategori bazl? ?neriler

### Seyahatler
- `POST /api/trips/pack` - Seyahat bavul haz?rla
- `GET /api/trips/trips` - Seyahat listesi
- `GET /api/trips/trips/{id}` - Seyahat detay?
- `DELETE /api/trips/trips/{id}` - Seyahat sil

## Veritaban? ?emas?

### Users
- Kullan?c? bilgileri ve premium durumu

### WardrobeItems
- K?yafet bilgileri (kategori, renk, stil, vb.)

### Outfits
- Kombinasyonlar ve stil skorlar?

### ShoppingRecommendations
- Al??veri? ?nerileri ve affiliate linkler

### Trips
- Seyahat bilgileri ve paketleme listeleri

## ML Modelleri

### K?yafet S?n?fland?rma
- Kategori ve alt kategori tahmini
- Renk analizi
- Stil etiketleme

### Kombinasyon ?nerisi
- Renk uyumlulu?u
- Stil uyumlulu?u
- Occasion uyumu

## Deployment

### Backend
```bash
docker-compose up -d
```

### Frontend
- React Native: Expo veya native build
- Web: Static hosting (Vercel, Netlify)

## G?venlik

- JWT authentication
- HTTPS zorunlu
- Rate limiting
- Input validation
- SQL injection korumas? (SQLAlchemy ORM)

## Gelecek ?zellikler

- ?? AR sanal deneme
- ?? Geli?mi? AI kombinasyon algoritmalar?
- ?? Sosyal ?zellikler (payla??m, takip)
- ?? Ma?aza entegrasyonlar?
- ?? Detayl? analytics
