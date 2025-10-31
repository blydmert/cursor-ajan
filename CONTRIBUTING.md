# Katk?da Bulunma Rehberi

AI M?zik Kompozisyon Asistan?'na katk?da bulunmay? d???nd???n?z i?in te?ekk?r ederiz! 

## Nas?l Katk?da Bulunabilirim?

### Hata Bildirimi

1. GitHub Issues'da mevcut hatalar? kontrol edin
2. Hata hen?z bildirilmemi?se, yeni bir issue a??n
3. Hatay? detayl? a??klay?n:
   - Ad?mlar (nas?l tekrarlan?r)
   - Beklenen davran??
   - Ger?ek davran??
   - Ekran g?r?nt?leri (varsa)
   - Taray?c?/OS bilgisi

### ?zellik ?nerisi

1. GitHub Issues'da ?neriyi aray?n
2. Yoksa, yeni bir "Feature Request" a??n
3. ?zelli?i detayl? a??klay?n:
   - Kullan?m senaryosu
   - Beklenen fayda
   - Olas? implementasyon y?ntemi

### Kod Katk?s?

1. **Fork ve Clone**
```bash
git clone https://github.com/yourusername/ai-music-composer.git
cd ai-music-composer
```

2. **Branch Olu?tur**
```bash
git checkout -b feature/amazing-feature
```

3. **Geli?tir**
- Kod standartlar?na uygun yaz?n
- Test ekleyin
- Dok?mantasyon g?ncelleyin

4. **Test Et**
```bash
# Backend testleri
cd backend
pytest

# Frontend testleri
cd frontend
npm test
```

5. **Commit**
```bash
git commit -m "feat: amazing new feature"
```

Commit mesaj? format?:
- `feat:` Yeni ?zellik
- `fix:` Hata d?zeltmesi
- `docs:` Dok?mantasyon
- `style:` Formatlamak, noktalama
- `refactor:` Kod refactoring
- `test:` Test ekleme
- `chore:` Bak?m i?leri

6. **Push ve Pull Request**
```bash
git push origin feature/amazing-feature
```

GitHub'da Pull Request a??n:
- De?i?iklikleri a??klay?n
- ?lgili issue'lar? referans verin
- Ekran g?r?nt?leri ekleyin (UI de?i?iklikleri i?in)

## Kod Standartlar?

### Python (Backend)
- PEP 8 standartlar?na uyun
- Type hints kullan?n
- Docstring'ler ekleyin
```python
def generate_melody(notes: List[int], duration: int) -> List[Dict]:
    """
    Generate a melody from given notes.
    
    Args:
        notes: List of MIDI note numbers
        duration: Duration in seconds
        
    Returns:
        List of note dictionaries with time and duration
    """
    pass
```

### JavaScript (Frontend)
- ESLint kurallar?na uyun
- PropTypes veya TypeScript kullan?n
- JSDoc yorumlar? ekleyin
```javascript
/**
 * Audio player component
 * @param {Object} props
 * @param {Object} props.musicData - Generated music data
 * @param {boolean} props.isPremium - Premium status
 */
function AudioPlayer({ musicData, isPremium }) {
  // ...
}
```

### CSS
- BEM metodolojisi kullan?n
- Responsive tasar?ma dikkat edin
- Modern CSS ?zellikleri kullan?n (Grid, Flexbox)

## Test Yazma

### Backend Tests
```python
def test_generate_music():
    request = {
        "keywords": ["energetic"],
        "duration": 30,
        "tempo": 120
    }
    response = client.post("/generate", json=request)
    assert response.status_code == 200
    assert "midi_data" in response.json()
```

### Frontend Tests
```javascript
test('renders music generator', () => {
  render(<MusicGenerator />);
  expect(screen.getByText(/M?zik Olu?tur/i)).toBeInTheDocument();
});
```

## Dok?mantasyon

- README g?ncellemeleri
- API dok?mantasyonu
- Kod yorumlar?
- Kullan?m ?rnekleri

## ?leti?im

- GitHub Issues: Sorular ve tart??malar i?in
- Email: dev@ai-music-composer.com
- Discord: [Topluluk sunucusu](#)

## Davran?? Kurallar?

- Sayg?l? ve yap?c? olun
- Farkl? g?r??lere a??k olun
- Yard?mc? ve destekleyici olun
- Profesyonel ileti?im kurun

## Lisans

Katk?lar?n?z MIT lisans? alt?nda lisanslanacakt?r.

---

Katk?lar?n?z i?in te?ekk?rler! ??
