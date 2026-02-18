from django.db import models

# Create your models here.
#categpry model - text and image 
#prodcut - itle, review, price,discount, price, instock, description, size (s,m,l,xl), colour, proodcut, specification,material
#cart - product, quantity
#cart product - cart, product, quantity
#order - cart, total price

class Category(models.Model):
    title = models.CharField(max_length=100) #title of the product example: shirt, trouser, shoe
    image = models.ImageField(upload_to="category_images/", null = True, blank = True, blank=True) #images of the product, null and blank means it not required
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=200)
    review = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    in_stock = models.BooleanField(default=True)
    description = models.TextField()
    size = models.CharField(max_length=10)
    colour = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to="product_images/", null=True, blank=True)
    specification = models.TextField()
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)       ]

    def __str__(self):
         return f"{self.quantity} of {self.product.title} in cart {self.cart.id}"


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)      

    def __str__(self):
        return f"Order for cart {self.cart.id} with total price {self.total_price}"    
