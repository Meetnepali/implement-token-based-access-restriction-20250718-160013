from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List
from app.dependencies import get_current_user

router = APIRouter()

class Product(BaseModel):
    id: int
    name: str
    price: float

fake_products_db = [
    {"id": 1, "name": "Apple", "price": 1.22},
    {"id": 2, "name": "Banana", "price": 0.99},
]

@router.get("/", response_model=List[Product])
def read_products():
    return fake_products_db

@router.post("/", response_model=Product)
def create_product(product: Product, current_user: dict = Depends(get_current_user)):
    fake_products_db.append(product.dict())
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product, current_user: dict = Depends(get_current_user)):
    for idx, p in enumerate(fake_products_db):
        if p["id"] == product_id:
            fake_products_db[idx] = product.dict()
            return product
    raise HTTPException(status_code=404, detail="Product not found")
