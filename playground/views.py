from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Q,F
from store.models import Product
from store.models import Customer, Collection, Order, OrderItem

# Create your views here.


def say_hello(request):
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    # unit price range: 20 -30
   # queryset = Product.objects.filter(unit_price__range=(20,30))

    # Customers with .com accounts
    #queryset = Customer.objects.filter(email__icontains='.com')

    # Collections that do not have a featured product
    #queryset = Collection.objects.filter(featured_product__isnull=True)

    # Product with low inventory
    #queryset = Product.objects.filter(inventory__lt=10)

    # Orders placed by customer with id = 1
    # queryset = Order.objects.filter(customer__id=1)

    # Order items for products in collection 3
    # queryset = OrderItem.objects.filter(product__collection__id=3)

    # Products: inventory <10 Or price <20
    # queryset = Product.objects.filter(Q(inventory__lt=20) | Q(unit_price__lt=20))
    
    # Products: inventory = price
    # queryset = Product.objects.filter(inventory=F('collection__id')).order_by('title')、

    # queryset = Product.objects.values('id','title','collection__title')
    # queryset = OrderItem.objects.values('product_id').distinct()


    # select_related (1)
    # prefetch_related (n)
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    
    #  Get the last 5 orders with their customer and items (incl product)
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    return render(request, 'hello.html', {'name': 'Jeo', 'products': list(queryset)})
