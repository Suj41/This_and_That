from django.shortcuts import render, redirect
from myapp.models import Department
from django.views import View
from myapp.models import AppUser




class DepartmentAdd(View):
      def get(self, request):
        return render(request, 'Department/add.html')
      
      def post(self, request):

        address=request.POST.get('address')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        depttype=request.POST.get('depttype')
        deptname=request.POST.get('deptname')
        appuser=request.session.get('appuser')
        print(address, appuser)
        dept=Department(deptname=deptname,
                        depttype=depttype,
                        address=address,
                        contact=contact,
                        email=email,
                        appuser= AppUser(id=appuser))
        dept.save()
        return redirect('/deptlist')
        
        
        
      
    #Customr Registartion Code
    #   def post(self, request):
    #     postData= request.POST
    #     deptname=postData.get('deptname')
    #     depttype=postData.get('depttype')
    #     address=postData.get('address')
    #     contact = postData.get('contact')
    #     email=postData.get('email')
    #     appuser=request.session.get['appuser']

    #     # Form Validation

    #     value={
    #             'deptname':deptname,
    #             'depttype':depttype,
    #             'address' : address,
    #             'contact': contact,
    #             'email':email,
    #         }

    #     department=Department(deptname=deptname, 
    #                               depttype=depttype,
    #                               address=address ,
    #                               contact=contact, 
    #                               email=email,
    #                               appuser= AppUser(id=appuser),
    #                               )
        
    #     error_msg=self.validateDepartment(department)

        

    #     if not error_msg:
    #         department.save()
    #         return redirect('deptlist')
    #     else:
    #         data={
    #             'value':value,
    #             'error':error_msg
    #         }    
    #         return render(request,'Department/add.html',data)
        
    #     # Customer Validation Code
    #   def validateDepartment(self, department):
    #         error_msg=None
    #         if len(department.deptname)<4:
    #             error_msg='First Name should be 4 character long.'
    #         elif len(department.depttype)<4:
    #             error_msg='Last Name should be 4 character long.'
    #         elif len(department.contact) != 10:
    #          error_msg = 'Phone Number should be 10 characters long.'

    
            