from fastapi import APIRouter, HTTPException
from app.models.models import supplier_pydanticIn, product_pydanticIn, supplier_pydantic, product_pydantic, Supplier, Product

router = APIRouter()


@router.post("/suppliers")
async def create_supplier(supplier_info: supplier_pydanticIn):
    supplier_obj = await Supplier.create(**supplier_info.dict(exclude_unset=True))
    response = await supplier_pydanticIn.from_tortoise_orm(supplier_obj)
    return {"status": "success", "data": response}


@router.get("/suppliers")
async def get_all_suppliers():
    # list of all suppliers
    response = await supplier_pydantic.from_queryset(Supplier.all())
    return {"status": "success", "data": response}

@router.get("/suppliers/{supplier_id}")
async def get_supplier_by_id(supplier_id: int):
    supplier_obj = await Supplier.get(id=supplier_id)
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {"status": "success", "data": response}

@router.put("/suppliers/{supplier_id}")
async def update_supplier_by_id(supplier_id: int, supplier_info: supplier_pydanticIn):
    supplier_obj = await Supplier.get(id=supplier_id)
    await supplier_obj.update_from_dict(supplier_info.dict(exclude_unset=True))
    await supplier_obj.save()
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {"status": "success", "data": response}

@router.delete("/suppliers/{supplier_id}")
async def delete_supplier_by_id(supplier_id: int):
    supplier_obj = await Supplier.get(id=supplier_id)
    await supplier_obj.delete()
    return {"status": "success", "data": "Supplier deleted successfully"}

