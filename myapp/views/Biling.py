from django.shortcuts import redirect,render, HttpResponse, get_list_or_404
from myapp.models import ProductCategory, Product, Department
from django.views import View



def addBill(request):
     
     if request.method=="GET":
        dept=request.session.get('department')
        dept=Department.get_department_by_id(dept[0].get('id'))
        
        print(dept)
        cart=request.session.get('cart')
        if not cart:
             request.session['cart']={}
        product=None
        category=ProductCategory.get_all_category()
        category_id=request.GET.get('category')
        if category_id:
            product=Product.get_all_products_by_categoryid(category_id)
        else:
            product=Product.get_all_products()
        context={}
        context['category']=category
        context['product']=product
        context['dept']=dept
        
        return render(request,'App/biling.html',context)
    
     if request.method=="POST":
          dept=request.session.get('department')
          dept=Department.get_department_by_id(dept[0].get('id'))
          product=request.POST.get('product')
          cart=request.session.get('cart')
          remove=request.POST.get('remove')
          if cart:
               quantity=cart.get(product)
               if quantity is not None:
                    if remove:
                        if quantity is not None:
                             cart.pop(product, None)
                        else:
                            cart[product]=quantity-1
                    else:
                        cart[product]=quantity+1
               else:
                    cart[product]=1
          else:
               cart={}
               cart[product]=1
          request.session['cart']=cart
          print('I am a ',request.session['cart'])
          return redirect('/biling')
     context={
         'dept':dept
     }
     return render(request,'App/biling.html',context)
     

def bill(request):
     
     if request.method=="GET":
        dept=request.session.get('department')
        dept=Department.get_department_by_id(dept[0].get('id'))
        ids=list(request.session.get('cart').keys())
        products=Product.get_product_by_id(ids)
        context={
           'products':products,
           'dept':dept
        }
        return render(request,'App/bill.html',context=context)
     if request.method=="POST":
         dept=request.session.get('department')
         dept=Department.get_department_by_id(dept[0].get('id'))
         contact = request.POST.get('contact')
         print('Helloe World', contact)
        # Process the product data
         cart=request.session.get('cart')
         products=Product.get_product_by_id(list(cart.keys()))
         print(cart, products)

     #     for product in products:
     #        order=Order(customer= Customer(id=customer),
     #                    product=product,
     #                    price=product.price,
     #                    address=address,
     #                    phone=phone,
     #                    quantity=cart.get(str(product.id)))
     #        order.PlaceOrder()
         request.session['cart']={}
     #     return redirect('/biling')
     return render(request,'App/bill.html',context=context)