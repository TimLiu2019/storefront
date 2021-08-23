from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Collection)

# register Product model
admin.site.register(models.Product)