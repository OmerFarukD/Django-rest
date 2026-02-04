from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import  mixins
from .models import Comment
from .serializers import CommentSerializer



class CommentListByProductView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        id = self.kwargs.get('id')
        serializer.save(product_id = id)

    def get_queryset(self):
        id = self.kwargs['id']
        return Comment.objects.filter(product_id=id)


class CommentDetailsView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

