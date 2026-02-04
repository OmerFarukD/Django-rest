from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer


# Create your views here.

@api_view(['GET','POST'])
def product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def product_details(request, id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return Response({'Error': "Ürün Bulunamadı"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    if request.method == 'PUT':
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
