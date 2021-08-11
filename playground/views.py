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
    queryset = Product.objects.filter(unit_price__range=(20,30))

    
  
    return render(request, 'hello.html', {'name': 'Jeo','products':list(queryset)})
