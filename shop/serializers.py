from rest_framework import serializers
from .models import Category, Product, News


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    slug = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data("name", instance.name)
        instance.slug = validated_data("slug", instance.slug)
        instance.save()

        return instance


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField(read_only=True)
    category_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    slug = serializers.CharField(max_length=100)
    image = serializers.ImageField(read_only=True)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    created = serializers.DateTimeField(read_only=True)
    uploaded = serializers.DateTimeField(read_only=True)
    available = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_id = validated_data("category_id", instance.category_id)
        instance.name = validated_data("name", instance.name)
        instance.slug = validated_data("slug", instance.slug)
        instance.image = validated_data("image", instance.image)
        instance.description = validated_data("description", instance.description)
        instance.price = validated_data("price", instance.price)
        instance.save()

        return instance


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()

        return instance
