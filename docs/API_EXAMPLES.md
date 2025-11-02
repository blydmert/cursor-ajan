# API Client Example

```python
import requests

BASE_URL = "http://localhost:8000"

# Kombinasyon ?nerisi al
response = requests.post(
    f"{BASE_URL}/api/combinations/suggest",
    json={
        "occasion": "i?",
        "preferred_items": [1, 2],  # Mavi ceket ve bej pantolon ID'leri
        "season": "sonbahar"
    }
)

outfits = response.json()
print(f"3 kombinasyon ?nerisi al?nd?: {len(outfits)}")

# Gard?rop ??elerini listele
response = requests.get(f"{BASE_URL}/api/wardrobe/items")
items = response.json()
print(f"Gard?ropta {len(items)} ??e var")

# K?yafet y?kle
with open("path/to/image.jpg", "rb") as f:
    response = requests.post(
        f"{BASE_URL}/api/wardrobe/items",
        files={"file": f},
        data={
            "name": "Mavi Ceket",
            "category": "d?? giyim"
        }
    )
    new_item = response.json()
    print(f"Yeni ??e eklendi: {new_item['id']}")

# Seyahat bavul haz?rla
from datetime import datetime, timedelta
start_date = datetime.now()
end_date = start_date + timedelta(days=5)

response = requests.post(
    f"{BASE_URL}/api/trips/pack",
    json={
        "name": "?stanbul ?? Seyahati",
        "destination": "?stanbul",
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "occasion": "i?"
    }
)
trip = response.json()
print(f"Seyahat olu?turuldu: {trip['name']}")
print(f"Paketleme listesi: {trip['items']}")
```
