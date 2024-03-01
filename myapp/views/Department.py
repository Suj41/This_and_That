from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Department
from django.views import View
from myapp.models import AppUser




def deptlist(request):
        department = Department.objects.all()
        request.session['department'] = list(department.values())
        print(department)
        context = {'department': department}
        return render(request, 'Department/DeptList.html', context=context)


def department(request, pk):
    dept=get_object_or_404(Department, pk=pk)
    context={
        'dept':dept
    }
    return render(request,'Department/dept-view.html',context=context)


def departmentupdate(request, pk):
    
    dept = get_object_or_404(Department, pk=pk)
    if request.method == "GET":
        context={
             'dept':dept
        }
        return render(request, 'Department/update.html', context=context)



    if request.method == 'POST':
        deptname=request.POST.get('deptname')
        depttype=request.POST.get('depttype')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        print('I am', dept.id)
        dept_instance=Department.objects.get(id=dept.id)
        try:
        # Retrieve the existing Department instance
                dept_instance = Department.objects.get(id=dept.id)
        
        # Update the fields
                dept_instance.deptname = deptname
                dept_instance.depttype = depttype
                dept_instance.address = address
                dept_instance.contact = contact
                dept_instance.email = email
        
        # Save the changes
                dept_instance.save()

                return redirect(f'/dept-view/{pk}')
        except Department.DoesNotExist:
                print('Department not found.')
      
def departmentdelete(request,pk):
    dept=get_object_or_404(Department,pk=pk)
    dept.delete()
    return redirect('/deptlist')



