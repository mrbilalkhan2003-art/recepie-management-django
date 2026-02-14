from django.shortcuts import render


from django.http import HttpResponse


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

