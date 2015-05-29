from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the compare website.")

# Create your views here.
def user(request):
    return HttpResponse("Hello, world. You're at the user website.")
    
# Create your views here.
def group(request):
    return HttpResponse("Hello, world. You're at the group website.")
