from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product

# Create your views here.


def say_hello(request):
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    product = Product.objects.filter(pk=0).first()

    
  
    return render(request, 'hello.html', {'name': 'Jeo'})
