from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")
    def __str__(self):#overriding the method to change the object name
        return self.product_name
class Contact(models.Model):
    message_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=40)
    customer_email=models.CharField(max_length=70,default="")
    customer_phone=models.CharField(max_length=11,default="")
    customer_query=models.CharField(max_length=500,default="")
    def __str__(self):
        return self.customer_name
    
class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=5000,default="")
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=14,default="")
class orderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    itemstamp=models.DateField(auto_now_add=True)
    def __str__(self):
        
        return str(self.order_id)
