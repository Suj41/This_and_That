from django.shortcuts import render,redirect, get_object_or_404
from django.views import    View
from myapp.models import Product, ProductCategory, Department
from decimal import Decimal



def productlist(request, pk):
        dept = get_object_or_404(Department, pk=pk)
        products = Product.objects.all()
        print(products)
        print('hello World')
        context = {'products': products,
                   'dept':dept}
        return render(request, 'App/product.html', context=context)
    
def productadd(request, pk):
    dept=get_object_or_404(Department, pk=pk)
    if request.method=="POST":
        productname=request.POST.get('productname')
        brandname=request.POST.get('brandname')
        category=request.POST.get('category')
        mrp=request.POST.get('mrp')
        weight=Decimal(request.POST.get('weight'))
        image=request.FILES.get('image')
        print(productname, brandname, image)
        category_instance = ProductCategory.objects.get(category=category)
        product=Product(productname=productname,
                        brandname=brandname,
                        category=category_instance,
                        mrp=mrp,
                        weight=weight,
                        image= image)
        product.save()
        return redirect(f'/productlist/{pk}')
    context={
         'dept':dept
    }
    
    return render(request, 'App/productadd.html', context=context)


