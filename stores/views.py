from django.shortcuts import render

# Create your views here.

from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product, Cart, CartProduct, Order
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, CartProductSerializer, Order


#CRUD CATEGORY -http method - get, post, put and delete request and response

#create and retrieve category. #post and get method
class CategoryListCreateAPIView(APIView):
#get method to retrieve category
    def get(self, request):
        try:    
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)  
        except Exception as e:
            return Response({"error": "An error occurred while retrieving categories"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#post method to create category
    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An error occurred while creating the category"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)      
       

 #retrieve, update and delete category # get, put and delete method
class CategoryRetrieveUpdateDeleteAPIView(APIView):
#get method to retrieve category by id
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "An error occurred while retrieving the category"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#update category
    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "An error occurred while updating the category"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#delete category    
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "An error occurred while deleting the category"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    