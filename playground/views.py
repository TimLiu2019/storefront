from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product
from store.models import Customer, Collection, Order, OrderItem

# Create your views here.


def say_hello(request):
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    #unit price range: 20 -30
   # queryset = Product.objects.filter(unit_price__range=(20,30))

    # Customers with .com accounts
    #queryset = Customer.objects.filter(email__icontains='.com')
    
 
    #Collections that do not have a featured product
    #queryset = Collection.objects.filter(featured_product__isnull=True)

    #Product with low inventory
    #queryset = Product.objects.filter(inventory__lt=10)

    # Orders placed by customer with id = 1
    # queryset = Order.objects.filter(customer__id=1)

    # Order items for products in collection 3
    queryset = OrderItem.objects.filter(product__collection__id=3)


  
    return render(request, 'hello.html', {'name': 'Jeo','products':list(queryset)})
