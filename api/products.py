from fastapi import APIRouter

from models import Product

router = APIRouter(prefix="/products")


@router.get(
    path="/",
    summary="Get all products",
)
def get_products() -> list[Product]:
    return Product.get_all()


@router.get(
    path="/{product_id}",
    summary="Get product by id",
)
def get_product(product_id: int) -> Product:
    return Product.get_by_id(product_id)
