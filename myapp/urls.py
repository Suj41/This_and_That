from django.urls import path
from .views.Show import show
from .views.Signup import Signup
from .views.Login import Login,logout
from .views.Department import  deptlist, department, departmentupdate, departmentdelete
from .views.DepartmentAdd import  DepartmentAdd
from .views.UserDashboard import  userdashboard
from .views.Product import productadd, productlist
from .views.Batch import batchadd,batchlist
from .views.Customer import customeradd, customerlist
from .views.Biling import addBill,bill

urlpatterns=[
    path('',show, name='show'),
    path('signup',Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('deptlist', deptlist, name='deptlist'),
    path('deptadd', DepartmentAdd.as_view(), name='deptadd'),
    path('dept-view/<int:pk>', department, name='dept-view'),
    path('dept-update/<int:pk>', departmentupdate, name='dept-update'),
    path('dept-delete/<int:pk>', departmentdelete, name='dept-delete'),
    path('logout', logout, name='logout'),
    path('userdash', userdashboard,name='userdash'),
    path('productlist/<int:pk>',productlist,name='productlist'),
    path('productadd/<int:pk>',productadd,name='productadd'),
    path('batchlist/<int:pk>',batchlist,name='batchlist'),
    path('batchadd/<int:pk>',batchadd,name='batchadd'),
    path('customerlist/<int:pk>',customerlist,name='customerlist'),
    path('customeradd/<int:pk>',customeradd,name='customeradd'),
    path('biling',addBill,name='biling'),
    path('bill',bill,name='bill'),
   

]