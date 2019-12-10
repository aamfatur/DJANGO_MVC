from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'alfa/index.html',{})

def blog(request):
    return render(request, 'alfa/blog.html',{})

def mentee(request):
    return render(request, 'alfa/mentee.html',{})

def mentor(request):
    return render(request, 'alfa/mentor.html',{})

def author(request):
    return render(request, 'alfa/author.html',{})