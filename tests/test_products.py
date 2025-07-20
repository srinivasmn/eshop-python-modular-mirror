
---

###  Optional: `tests/test_products.py`
```python
from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
