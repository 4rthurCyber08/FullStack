from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response # type: ignore
from .serializer import ProductSerializer
from .models import Product

# Create your views here.
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_details(request, pk):
    products = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(products)
    return Response(serializer.data)