from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def set_cookie(request):
    reponse= HttpResponse("Cookie Set!")
    reponse.set_cookie('username', 'DjangoMaster')
    return reponse

def get_cookie(request):
    username= request.COOKIES.get('username', 'Guest')
    return HttpResponse(f"Hello, {username}!")

def delete_cookie(request):
    pass