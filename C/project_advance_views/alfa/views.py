from django.shortcuts import render
from django.http import HttpResponse
from .models import Mentee, Mentor, Blog 

# Create your views here.
def index(request):
    return render(request, 'alfa/index.html',{})

def blog(request):
    blog_data = Blog.objects.all()
    return render(request, 'alfa/blog.html',{'blog_data' : blog_data})

def mentee(request):
    mentee_data = Mentee.objects.all()
    return render(request, 'alfa/mentee.html',{'mentee_data' : mentee_data})

def mentor(request):
    mentor_data = Mentor.objects.all()
    return render(request, 'alfa/mentor.html',{'mentor_data' : mentor_data})

def author(request):
    return render(request, 'alfa/author.html',{})