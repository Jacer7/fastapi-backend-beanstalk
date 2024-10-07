
from fastapi import APIRouter, HTTPException
from app.models.models import supplier_pydanticIn, product_pydanticIn, supplier_pydantic, product_pydantic, Supplier, Product

router = APIRouter()


@router.post("/product/{supplier_id}")
async def add_product(supplier_id: int, product_info: product_pydanticIn):
    supplier = await Supplier.get(id=supplier_id)
    product_info = product_info.dict(exclude_unset=True) # convert json to dict
    product_info["revenue"] = product_info["quantity_sold"] * product_info["unit_price"]
    product_obj = await Product.create(**product_info, supplied_by=supplier)
    response = await product_pydantic.from_tortoise_orm(product_obj)
    return {"status": "success", "data": response}

@router.get("/product")
async def get_all_products():
    # list of all products
    response = await product_pydantic.from_queryset(Product.all())
    return {"status": "success", "data": response}

@router.get("/product/{product_id}")
async def get_product_by_id(product_id: int):
    product_obj = await Product.get(id=product_id)
    response = await product_pydantic.from_tortoise_orm(product_obj)
    return {"status": "success", "data": response}

@router.put("/product/{product_id}")
async def update_product_by_id(product_id: int, product_info: product_pydanticIn):
    product_obj = await Product.get(id=product_id)
    update_info = product_info.dict(exclude_unset=True)
    product_obj.name = update_info["name"]
    product_obj.quantity_in_stock = update_info["quantity_in_stock"]
    product_obj.revenue = update_info["quantity_sold"] * update_info["unit_price"] + update_info["revenue"]
    product_obj.quantity_sold += update_info["quantity_sold"] 
    product_obj.unit_price = update_info["unit_price"]
    product_obj.description = update_info["description"]
    await product_obj.save()
    response = await product_pydantic.from_tortoise_orm(product_obj)
    return {"status": "success", "data": response}

@router.delete("/product/{product_id}")
async def delete_product_by_id(product_id: int):
    product_obj = await Product.get(id=product_id) 
    await product_obj.delete()
    return {"status": "success", "data": "Product deleted successfully"}
