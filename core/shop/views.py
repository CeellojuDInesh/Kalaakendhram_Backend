from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category
from .serializers import CategoryWithProductsSerializer


class CategoryWithProductsAPIView(APIView):
    def get(self, request):
        categories = Category.objects.prefetch_related("products__variants").all()
        serializer = CategoryWithProductsSerializer(categories, many=True)
        return Response(serializer.data)
