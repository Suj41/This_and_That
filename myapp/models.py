from django.db import models

# Create your models here.
from django.db import models

class AppUser(models.Model):
    firstname=models.CharField(max_length=25, blank=False, null=False)
    lastname=models.CharField(max_length=25, blank=False, null=False)
    address=models.CharField(max_length=50, blank=False, null=False)
    contact=models.CharField(max_length=25, blank=False, null=False)
    email=models.CharField(max_length=50, blank=False, null=False)
    password=models.CharField(max_length=255, blank=False, null=False)

    def register(self):
        self.save()

    def isExist(self):
        if AppUser.objects.filter(email=self.email):
            return True
        return False
    
    @staticmethod
    def get_appuser_by_email(email):
        try:
            return AppUser.objects.get(email=email)
        except:
            return False
        

class Department(models.Model):
    deptname=models.CharField(max_length=50)
    depttype=models.CharField(max_length=25)
    address=models.CharField(max_length=50)
    contact=models.CharField(max_length=25)
    email=models.CharField(max_length=50)
    appuser=models.ForeignKey(AppUser, on_delete=models.CASCADE)

    def register(self):
        self.save()

    @staticmethod
    def get_department_by_appuser(appuser_id):
        return Department.objects.filter(appuser=appuser_id)   
    @staticmethod
    def get_department_by_id(dept):
        try:
            return Department.objects.get(id=dept)
        except:
            return False    
    
class ProductCategory(models.Model):
    category=models.CharField(max_length=50)
    def register(self):
        self.save()
    @staticmethod
    def get_all_category():
        return ProductCategory.objects.all()   

class Product(models.Model):
    productname=models.CharField(max_length=50)
    brandname=models.CharField(max_length=50)
    category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=1)
    mrp=models.DecimalField(max_digits=5, decimal_places=2,default=0)
    weight=models.DecimalField(max_digits=3, decimal_places=3,default=0)
    image= models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
        
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)
    
    

    def register(self):
        self.save()


class Batch(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    batchnumber=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    batchcost=models.DecimalField(max_digits=8, decimal_places=2,default=0)
    batchdate=models.DateField(auto_now_add=True)
    manufacturedate=models.DateField(auto_now=True)
    expirydate=models.DateField(auto_now=True)

    def register(self):
        self.save()


class Customer(models.Model):
    firstname=models.CharField(max_length=25, blank=False, null=False)
    lastname=models.CharField(max_length=25, blank=False, null=False)
    address=models.CharField(max_length=50, blank=False, null=False)
    contact=models.CharField(max_length=25, blank=False, null=False)
    gender=models.CharField(max_length=6, blank=False, null=False)
    department=models.ForeignKey(Department, on_delete=models.CASCADE, default=1)

    def register(self):
        self.save()

class BilingSystem(models.Model):
    transaction_id=models.IntegerField(default='1000')
    contact=models.CharField(max_length=25, )
    product=models.CharField(max_length=250, blank=False, null=False)
    quantity=models.IntegerField(default=0)
    category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=1)
    price=models.DecimalField(max_digits=8, decimal_places=2,default=0)
    total=models.DecimalField(max_digits=8, decimal_places=2,default=0)
    department=models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    date=models.DateField(auto_now_add=True)
    


 
       