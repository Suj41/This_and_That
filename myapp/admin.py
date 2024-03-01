from django.contrib import admin
from .models import AppUser, Department, ProductCategory, Product, Batch, Customer
# Register your models here.
class AdminAppUser(admin.ModelAdmin):
    list_display=['firstname','lastname','address','contact','email','password']
class AdminDepartment(admin.ModelAdmin):
    list_display=['deptname','depttype','address','contact','email','appuser']

class AdminProductCategory(admin.ModelAdmin):
    list_display=['category']

class AdminProduct(admin.ModelAdmin):
    list_display=['productname', 'brandname', 'category','mrp', 'weight', 'image']

class AdminBatch(admin.ModelAdmin):
    list_display=['product', 'batchnumber', 'quantity','batchcost', 'batchdate', 'manufacturedate','expirydate']

class AdminCustomer(admin.ModelAdmin):
    list_display=['firstname', 'lastname', 'gender','address', 'contact', 'department']

admin.site.register(Customer,AdminCustomer)

admin.site.register(Batch,AdminBatch)

admin.site.register(Product,AdminProduct)

admin.site.register(ProductCategory,AdminProductCategory)

admin.site.register(AppUser,AdminAppUser)

admin.site.register(Department,AdminDepartment)



