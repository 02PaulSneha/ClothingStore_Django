from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("Hello, I am sneha!") # this return only strin
    return render(request , 'website/index.html') # this return templates

def about(request):
    #return HttpResponse("This is my about page")
     return render(request , 'website/about.html')


def contact(request):
    #return HttpResponse("This is my contact page")
     return render(request , 'website/contact.html')


def  help_center(request):
    #return HttpResponse("This is my help center page")
     return render(request , 'website/help_center.html')

