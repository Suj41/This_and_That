from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Customer, Department
from decimal import Decimal



def customerlist(request, pk):
        dept=get_object_or_404(Department, pk=pk)
        customers = Customer.objects.all()
        print(customers)
        print('hello World')
        context = {'customers': customers,
                   'dept':dept}
        return render(request, 'App/customer.html', context=context)
    
def customeradd(request,pk):
    dept=get_object_or_404(Department,pk=pk)
    customers = Customer.objects.all()

    if request.method=="POST":
        print(request.POST) 
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        department=dept
        
        
        customer=Customer(firstname=firstname,
                        lastname=lastname,
                        address=address,
                        contact=contact,
                        gender=gender,
                        department= department)
        customer.save()
        return redirect(f'/customerlist/{pk}')
    context={'customers': customers,
         'dept':dept}
    return render(request, 'App/customeradd.html', context=context)


