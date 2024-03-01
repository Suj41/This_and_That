from django.shortcuts import render


def userdashboard(request):
    return render(request, 'App/header.html')