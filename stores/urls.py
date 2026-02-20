from django.urls import path
from . import views


urlpatterns = [
    path("categories/", views.CategoryListCreateAPIView.as_view(), name="category-list-create"),
    path("categories/<int:id>/", views.CategoryRetrieveUpdateDeleteAPIView.as_view(), name="category-retrieve-update-delete"),
    path("categories/view/", views.category_list_view, name="category-list-view"),
    path("products/", views.ProductListCreateAPIView.as_view(), name="product-list-create"),
    path("products/<int:id>/", views.ProductRetrieveUpdateDeleteAPIView.as_view(), name="product-retrieve-update-delete"),
    path("products/view/", views.product_list_view, name="product-list-view"),
    # path("cart/", views.CartListCreateAPIView.as_view(), name="cart-list-create"),
    # path("cart/<int:id>/", views.CartRetrieveUpdateDeleteAPIView.as_view(), name="cart-retrieve-update-delete"),
    # path("cart-products/", views.CartProductListCreateAPIView.as_view(), name="cart-product-list-create"),
    # path("cart-products/<int:id>/", views.CartProductRetrieveUpdateDeleteAPIView.as_view(), name="cart-product-retrieve-update-delete"),
    # path("orders/", views.OrderListCreateAPIView.as_view(), name="order-list-create"),
    # path("orders/<int:id>/", views.OrderRetrieveUpdateDeleteAPIView.as_view(), name="order-retrieve-update-delete"),
]
