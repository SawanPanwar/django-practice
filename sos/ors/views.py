from django.http import HttpResponse
from django.shortcuts import render


def test_ors(request):
    return HttpResponse('<h1>ORS APP</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    print(request.GET.get('firstName'))
    print(request.GET.get('lastName'))
    print(request.GET.get('loginId'))
    print(request.GET.get('password'))
    print(request.GET.get('dob'))
    print(request.GET.get('address'))
    return render(request, 'registration.html')


def user_signin(request):
    return render(request, 'login.html')
