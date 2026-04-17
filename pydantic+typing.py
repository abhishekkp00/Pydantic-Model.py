from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    total_price: float
    discount_code: Optional[str] = None  # Optional field with default value of None
    quantities: Dict[str, int]  # Dictionary to hold item names and their quantities

class BlogPost(BaseModel):
    title: str
    content: str
    content_url: Optional[str] = None  # Optional field for a URL to the content
    
cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "total_price": 1500.00,
    "quantities": {"Laptop": 1, "Mouse": 2, "Keyboard": 1}
}

cart = Cart(**cart_data)
print(cart)