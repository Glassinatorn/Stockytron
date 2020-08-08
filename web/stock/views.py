from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"test": 32}
    return render(request, 'stock/index.html', context)
