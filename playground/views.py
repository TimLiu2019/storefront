from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, ExpressionWrapper,DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
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
    # queryset = Customer.objects.filter(email__icontains='.com')

    # Collections that do not have a featured product
    # queryset = Collection.objects.filter(featured_product__isnull=True)

    # Product with low inventory
    # queryset = Product.objects.filter(inventory__lt=10)

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
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # Aggregate
   #  result = Product.objects.aggregate(
   #      count=Count('id'), min_price=Min('unit_price'))

    # Aggregate how many orders do we have
    #  result = Order.objects.aggregate(count=Count('id'))

    # Aggregate how many units of product 1 have we sold
    # result = Order.objects.aggregate(count=Count('id'))

    # How many units of product 1 have we sold
    # result = OrderItem.objects.filter(product_id=1).aggregate(unit_sold=Sum('quantity'))

    # How many orders have customer 1 placed?
    # result = Order.objects.filter(customer__id=1).aggregate(count=Count('id'))

    # what is the min, max and avg price of products in collection 1?
    # result = Product.objects.filter(collection__id=3).aggregate(min_price=Min('unit_price'),avg_price=Avg('unit_price'),max_price=Max('unit_price'))

    # queryset = Customer.objects.annotate(new_id=F('id') + 1)

   #  queryset = Customer.objects.annotate(
   #      # concat
   #      full_name=Func(F('first_name'), Value(
   #          ' '), F('last_name'), function='CONCAT')
   #  )
   #  queryset = Customer.objects.annotate(
   #      # CONCAT
   #       full_name=Concat('first_name', Value(
   #          ' '), 'last_name')
   #    )

   #  queryset = Customer.objects.annotate(
   #      # CONCAT
   #       orders_count=Count('order')
   #    )

   #  discounted_price=ExpressionWrapper(F('unit_price')*0.8, output_field=DecimalField())
   #  queryset = Product.objects.annotate(
        
   #       discounted_price=discounted_price
   #    )
    # Customers with their last order ID
   #  queryset = Customer.objects.annotate(last_order_id=Max('order__id'))

    # Collections and count of their products
   #  queryset = Collection.objects.annotate(product_count=Count('product'))

   # Customers with more than 5 orders
   # queryset = Customer.objects.annotate(order_count=Count('order')).filter(order_count__gt=5)
  
   # Customers and the total amount they have spent
   #  queryset = Customer.objects.annotate(
   #     total_spent=Sum(
   #        F('order__orderitem__unit_price') *
   #        F('order__orderitem__quantity')
   #     )
   #  )

   # Top 5 best-selling products and their total sales
    queryset = Product.objects.annotate(
       total_sales=Sum(
          F('orderitem__unit_price')*
          F('orderitem__quantity'))).order_by('-total_sales')[:5]

    # return render(request, 'hello.html', {'name': 'Jeo', 'result': result})
    return render(request, 'hello.html', {'name': 'Jeo', 'products': list(queryset)})
