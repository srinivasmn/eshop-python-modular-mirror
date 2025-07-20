# eShop Python Modular Mirror (FastAPI + CQRS)

This is a FastAPI-based backend skeleton that mirrors a .NET-style modular monolith architecture using Python.  
CQRS, Command Handlers, Domain Separation, and routing abstraction included.

## Project Structure

eshop-python-modular-mirror/
├── app/
│ ├── api/ # FastAPI entry point + routes
│ ├── application/ # CQRS command handlers
│ ├── domain/ # Data models / Entities
│ └── infrastructure/ # (Planned: DB, messaging, etc.)
├── tests/ # (To be added)
├── requirements.txt
├── .env.example
├── README.md


## How to Run (Dev)

```bash
# Step 1: Clone and enter
git clone <your-repo-url>
cd eshop-python-modular-mirror

# Step 2: Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the server
uvicorn app.api.main:app --reload

# Test the endpoint
curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d "{\"customer_id\":101,\"product_id\":22,\"quantity\":5}"


# Response should be:
{
  "order_id": 1,
  "status": "Created",
  "customer_id": 101
}

---

#### 4. **Postman Collection (Optional, Bonus)**
If time permits, create a Postman request for `/orders`:
- Method: POST
- URL: `http://localhost:8000/orders`
- Body:
  ```json
  {
    "customer_id": 101,
    "product_id": 22,
    "quantity": 5
  }



