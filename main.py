from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
# from tortoise import fields, models
# from app.models.models import supplier_pydanticIn, product_pydanticIn, supplier_pydantic, product_pydantic, Supplier, Product
# from typing import Type

from app.api.v1.endpoints.supplier import router as suppliers_router
from app.api.v1.endpoints.product import router as products_router

app = FastAPI()

app.include_router(suppliers_router, prefix="/api/v1/supplier", tags=["Supplier"])
app.include_router(products_router, prefix="/api/v1/product", tags=["Product"])

@app.get("/")
async def root():
    return {"message": "Hello Inventory!"}


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models.models"]},  # This should match your folder structure
    generate_schemas=True,
    add_exception_handlers=True
)
