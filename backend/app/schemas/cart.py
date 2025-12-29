from typing import Optional

from pydantic import BaseModel, Field


class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Unique product ID")
    quantity: int = Field(...,gt=0, description="Quantity(must be greater than 0)")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Unique product ID")
    quantity: int = Field(..., gt=0, description="Quantity(must be greater than 0)")

class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product_name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Quantity in cart")
    subtotal: float = Field(..., description="Total price for this item(price + quantity)")

    image_url: Optional[str] = Field(None, description="Product image URL")


