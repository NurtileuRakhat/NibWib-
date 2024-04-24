from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from django.db.models import Q
# from django.contrib.auth import get_user

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
class CategoryList(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductList(APIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request):
        query = request.query_params.get('search')
        if query:
            products = Product.objects.filter(name__icontains=query)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated|ReadOnly])
def get_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as error:
        return Response({'message': str(error)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response({'message': 'successfully deleted'}, status=status.HTTP_204_NO_CONTENT)

class Category_products(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]

    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        serializer = ProductSerializer(category.product_set.all(), many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated|ReadOnly])
def get_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as error:
        return Response({'message': str(error)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response({'message': 'successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
