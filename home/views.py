from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home/dashboard.html')
def products(request):
    return HttpResponse('Products Page')
def customer(request):
    return HttpResponse('Customer Page')