from django.shortcuts import render

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

