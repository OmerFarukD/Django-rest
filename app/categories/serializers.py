from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[UniqueValidator(queryset=Category.objects.all())])
    description = serializers.CharField(allow_blank=True, allow_null=True)

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('İsim ve açıklama alanı aynı olamaz.')
        return data

    def validate_name(self,value):
        if len(value) < 2:
            raise serializers.ValidationError('İsim Alanı minimum 2 haneli olmalıdır.')
        return value



    def create(self, validated_data):
        return  Category.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

