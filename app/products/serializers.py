from rest_framework import serializers

from .models import Product
from rest_framework.validators import UniqueValidator
from categories.models import Category
import re

from comments.serializers import CommentSerializer


class ProductSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)
    name = serializers.CharField(max_length=200, validators=[UniqueValidator(queryset=Product.objects.all())])
    slug = serializers.CharField(validators=[UniqueValidator(queryset=Product.objects.all())])
    class Meta:
        model = Product
        fields = ['id','name','description','price','stock','slug','category','comments']


    def validate_name(self,value:str):
        if len(value.strip())<3:
            raise serializers.ValidationError('Ürün adı minimum 3 haneli olmalıdır.')
        return value

    def validate_price(self,value):
        if value<0:
            raise serializers.ValidationError('Ürün fiyatı 0 dan küçük olamaz.')

        if value>100000:
            raise  serializers.ValidationError('Ürün Fiyatı Çok yüksek')

        return value

    def validate_stock(self,value):
        if value<0:
            raise serializers.ValidationError('Stok bilgisi 0 dan küçük olamaz.')
        return value

    def validate_slug(self,value):
        if not re.match('^[a-z0-9]+(?:-[a-z0-9]+)*$'):
            raise serializers.ValidationError('Slug biçimine uymuyor.')
        return value

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price',instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance
