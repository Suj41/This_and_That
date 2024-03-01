from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from myapp.models import AppUser

from django.views import View


class Login(View):
      return_url=None
      def get(self, request):
            Login.return_url=request.GET.get('return_url')
            return render(request, 'login.html')
      def post(self, request):
            email=request.POST.get('email')
            password=request.POST.get('password')

            appuser=AppUser.get_appuser_by_email(email)

            error_msg= None
            if appuser:
                flag=check_password(password, appuser.password)
                if flag:
                      request.session['appuser']=appuser.id
                      if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)

                      else:
                         Login.return_url=None
                         return redirect('deptlist')
                else:
                      error_msg='Email or Password invalid'

            else:
                  error_msg='Email or Password Invalid'
            return render(request, 'login.html', {'error':error_msg}) 
            

def logout(request):
           request.session.clear()
           return redirect('login')