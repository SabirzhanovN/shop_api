from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('api/v1/categorylist', CategoryApiView.as_view()),
    path('api/v1/categorylist/<int:pk>', CategoryApiView.as_view()),
    path('api/v1/categorylist/update/<int:id>', CategoryApiView.as_view()),

    path('api/v1/categorylist/products', ProductApiView.as_view()),
    path('api/v1/categorylist/products/<int:pk>', ProductApiView.as_view()),
    path('api/v1/categorylist/products/update/<int:pk>', ProductApiView.as_view()),

    path('api/v1/newslist', NewsApiView.as_view()),
    path('api/v1/newslist/<int:pk>', NewsApiView.as_view()),
    path('api/v1/newslist/update/<int:pk>', NewsApiView.as_view())
]
