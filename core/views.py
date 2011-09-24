from django.shortcuts import render

def homepage_handler(request):
    return render(request,'homepage.html',{})
