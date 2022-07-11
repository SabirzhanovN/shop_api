from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, News
from .serializers import CategorySerializer, ProductSerializer, NewsSerializer


def index(request):
    return HttpResponse('<h1>news: api/v1/newslist</h1>\t<h1>Products: api/v1/categorylist</h1>')


class CategoryApiView(APIView):
    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        if id:
            w = Product.objects.filter(category_id=id)
            if len(w) == 0:
                return Response({"error": "Objects does not exist"})
            else:
                return Response({"posts": ProductSerializer(w, many=True).data})

        w = Category.objects.all()
        return Response({'posts': CategorySerializer(w, many=True).data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Object has not exists"})

        serializer = CategorySerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()

        return Response({"post": serializer.data})

class ProductApiView(APIView):
    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        if id:
            try:
                w = Product.objects.get(pk=id)
                return Response({"post": ProductSerializer(w).data})
            except Product.DoesNotExist:
                return Response({"error": "Object has not exist"})


        w = Product.objects.all()
        return Response({'posts': ProductSerializer(w, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Object has not exist"})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()

        return Response({"post": serializer.data})

    def delete(self, request, id):
        w = Product.objects.get(pk=id)
        w.delet()

        return Response({"error": "Object has not exist"})


class NewsApiView(APIView):
    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        if id:
            try:
                w = News.objects.get(pk=id)
                return Response({"post": NewsSerializer(w).data})
            except News.DoesNotExist:
                return Response({"error": "Object has not exist"})

        w = News.objects.all()
        return Response({"posts": NewsSerializer(w, many=True).data})

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = News.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = NewsSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()

        return Response({"post": serializer.data})

    def delete(self, request, id):
        w = News.objects.get(pk=id)
        w.delete()

        return Response({"post": "Object has not exist"})
