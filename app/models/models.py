from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=40, nullable=False)
    quantity_in_stock = fields.IntField(default=0)
    quantity_sold = fields.IntField(default=0)
    unit_price = fields.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    revenue = fields.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    description = fields.TextField(null=True)
    supplied_by = fields.ForeignKeyField("models.Supplier", related_name="goods_supplied")

    def __str__(self):
        return self.name
    
class Supplier(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20, nullable=False)
    description = fields.TextField(null=True)
    company = fields.CharField(max_length=40)
    email = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
    
# create pydantic models
product_pydantic = pydantic_model_creator(Product, name="Product")
product_pydanticIn = pydantic_model_creator(Product, name="ProductIn", exclude_readonly=True)
supplier_pydantic = pydantic_model_creator(Supplier, name="Supplier")
supplier_pydanticIn = pydantic_model_creator(Supplier, name="SupplierIn", exclude_readonly=True)