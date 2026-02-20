from rest_framework import serializers
from .models import Category, Product #, Cart, CartProduct, Order

#CATEGORY SERIALIZERS
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

#PRODUCT SERIALIZERS
from .models import Product 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

# #CART SERIALIZERS
# from .models import Cart
# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = "__all__"

# #CART PRODUCT SERIALIZERS
# from .models import CartProduct
# class CartProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartProduct
#         fields = "__all__"

# #ORDER SERIALIZERS
# from .models import Order
# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = "__all__"