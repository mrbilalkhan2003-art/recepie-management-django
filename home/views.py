from django.shortcuts import render ,redirect


from django.http import HttpResponse
from .utils import send_email_to_client

def send_email(request):
    send_email_to_client()
    return redirect('/')


def home(request):

    peoples = [
        {'name':'bilal khan','age': 23 },
        {'name':'khan','age': 18 },
        {'name':'ramesh khan','age': 25 },
        {'name':'kamleesh khan','age': 17 }
    ]
    

    return render(request ,"index.html" , context= {'page':'Django 2026 Tutorial ','peoples':peoples})

def About(request):
    context = {'page':'About'}
    return render(request ,"about.html",context)

def Contact(request):
    context = {'page':'Contact'}
    return render(request ,"contact.html",context)

