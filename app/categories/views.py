from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import  Response
from rest_framework import status
class CategoryListAV(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetilsAV(APIView):
    def get(self, request, id):
        try:
            category = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return Response({"Error" : "Kategori Bulunamadı"},status= status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, id):
        category = Category.objects.get(pk=id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)




