from django.http import HttpResponse
from django.shortcuts import render

from . import bot_client

# Create your views here.

def index(request):
    data = bot_client.GetData()
    context = {
                "name": data.StockName,
                "price": data.price
              }
    return render(request, 'stock/index.html', context)
