# Install
Python >= 3.7 required

`pip install -r requirements.txt`

# Run Demo
`python manage.py runserver --nothreading`

# API
## Create X discount codes for brand
**POST** `/api/v1/coupons`

Creates new codes for brand using discount and amount provided
- Response `201 Created`
- Request parameters:
  - brand_id: int
  - data: dict
    - discount: float
    - amount: int
    
**Validation**:
* **discount** - float value `0.0 ≤ discount ≤ 1.0`
    - Response: `400 Bad Request`
    - Message: `"Discount should be float number 0.0 <= value <= 1.0"`
* **brand_id** - value exists
    - Response: `404 Not Found` # Not available in Demo
* **amount** - integer value `amount ≥ 0`
    - Response: `400 Bad Request`
    - Message: `"Amount should be an integer >= 0"`

### Demo Example: 
```
curl -sb -o /dev/null -D - -H "Content-Type: application/json" -d '{"brand_id": 123, "data": {"discount": 0.02, "amount": 100}}' http://127.0.0.1:8000/api/v1/coupons
```
## Claim discount code
**POST** `/api/v1/coupons/claim`

User claims new code with given discount from brand
- Response: `200 OK`
  - discount_code: str
  - discount: float
  - claimed: datetime
- Request:
  - brand_id: int
  - data: dict
    - email:str
    - discount:float

**Validation**:
* **discount** - float value `0.0 ≤ discount ≤ 1.0`
    - Response: `400 Bad Request`
    - Message: `"Discount should be float number 0.0 <= value <= 1.0"`
* **brand_id** - value exists
    - Response: `404 Not Found` # Not available in Demo
* **email** - not exists
    - Response: `409 Conflict`
    - Message: `"User [email] already claimed a coupon"` # Demo email `claimed@test.com`

### Demo Example: 
```
curl -sb -o /dev/null -D - -H "Content-Type: application/json" -d '{"brand_id": 123, "data": {"discount": 0.02, "email": "some@email.com"}}' http://127.0.0.1:8000/api/v1/coupons/claim
```