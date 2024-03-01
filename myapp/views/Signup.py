from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from myapp.models import AppUser
from django.views import View



class Signup(View):
      def get(self, request):
            return render(request, 'signup.html')
      
    #Customr Registartion Code
      def post(self, request):
        postData= request.POST
        firstname=postData.get('firstname')
        lastname=postData.get('lastname')
        address=postData.get('address')
        contact = postData.get('contact')
        email=postData.get('email')
        password=postData.get('password')
        cpassword=postData.get('cpassword')

        # Form Validation

        value={
                'firstname':firstname,
                'lastname':lastname,
                'address' : address,
                'contact': contact,
                'email':email,
            }

        appuser=AppUser(firstname=firstname, 
                                  lastname=lastname,
                                  address=address ,
                                  contact=contact, 
                                  email=email,
                                  password=password,
                                  )
        
        error_msg=self.validateAppUser(appuser)

        if password != cpassword:
            error_msg="re-enter password"

        if not error_msg:
            appuser.password=make_password(appuser.password)
            appuser.register()
            return redirect('login')
        else:
            data={
                'value':value,
                'error':error_msg
            }    
            return render(request,'signup.html',data)
        
        # Customer Validation Code
      def validateAppUser(self, appuser):
            error_msg=None
            if len(appuser.firstname)<4:
                error_msg='First Name should be 4 character long.'
            elif len(appuser.lastname)<4:
                error_msg='Last Name should be 4 character long.'
            elif len(appuser.contact) != 10:
             error_msg = 'Phone Number should be 10 characters long.'

            elif len(appuser.password)<6 or len(appuser.password)>14 :
                error_msg='Password length should be between 6-14 character.'
            elif appuser.isExist():
                error_msg='Email Address already exist.'
            
     

            
            