from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Category,Product

def hello_world(request):
    return render_to_response("helloDJ/home.html"),{"product" : Product.objects.all()})