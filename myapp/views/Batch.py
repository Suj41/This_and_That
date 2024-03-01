from django.shortcuts import render,redirect, get_object_or_404
from myapp.models import Product, Batch,Department
from decimal import Decimal



def batchlist(request, pk):
        dept = get_object_or_404(Department, pk=pk)

        batchs = Batch.objects.all()
        print(batchs)
        print('hello World')
        context = {'batchs': batchs,
                   'dept':dept}
        return render(request, 'App/batch.html', context=context)
    
def batchadd(request,pk):
    dept = get_object_or_404(Department, pk=pk)
    if request.method=="POST":
        print(request.POST) 
        productname=request.POST.get('productname')
        batchnumber=request.POST.get('batchnumber')
        quantity=int(request.POST.get('quantity'))
        batchcost=Decimal(request.POST.get('batchcost'))
        batchdate=request.POST.get('batchdate')
        manufacturedate=request.POST.get('manufacturedate')
        expirydate=request.POST.get('expirydate')
        product_instance = Product.objects.get(productname=productname)
        print(productname, product_instance, type(batchcost), batchnumber)
        batch=Batch(product=product_instance,
                        batchnumber=batchnumber,
                        quantity=quantity,
                        batchcost=batchcost,
                        batchdate=batchdate,
                        manufacturedate= manufacturedate,
                        expirydate=expirydate)
        batch.save()
        return redirect(f'/batchlist/{pk}')
    context={'dept':dept}
    return render(request, 'App/batchadd.html', context=context)


