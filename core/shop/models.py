from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Модель категории товаров
class Category(models.Model):
    """
       Model for product categories.

       Attributes:
           name (str): The name of the category.
           slug (str): Unique URL identifier for the category.

       Meta:
           verbose_name (str): Singular name for display in Django admin ('Category').
           verbose_name_plural (str): Plural name for display in Django admin ('Categories').

       Methods:
           __str__(): Returns the string representation of the category (its name).

       """
    CATEGORY_CHOICES = [
        ('MEN', 'Men'),
        ('WOMEN', 'Women'),
    ]
    name = models.CharField(choices=CATEGORY_CHOICES,
                            max_length=10,
                            unique=True,
                            help_text='Choose the category type: Men or Women')
    slug = models.SlugField(max_length=100,
                            unique=True,
                            help_text='Unique URL path segment for this category')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category_product'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    """
       Model for products available in the store.

       Attributes:
           name (str): The name of the product.
           slug (str): Unique URL identifier for the product.
           description (str, optional): Description of the product.
           price (Decimal): Price of the product.
           stock (int): Number of units available in stock.
           category (Category): ForeignKey to Category model, specifying the product's category.
           size (str): Size options for the product (e.g., S, M, L, XL).
           color (str): Color options for the product (e.g., Red, Blue, Black).
           views (int): Number of times the product has been viewed.
           rating (int): Rating of the product, ranging from 0 to 5.
           likes (int): Number of likes received for the product.

       Methods:
           __str__(): Returns the string representation of the product (its name).

       """
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True,
                                   null=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=100)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='products')
    size = models.CharField(max_length=10,
                            choices=SIZE_CHOICES)
    color = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)
    rating = models.PositiveSmallIntegerField(default=0,
                                              help_text='Rating from 0 to 5')
    likes = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        db_table = 'product'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
#
# # Модель клиента
# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#
#     def __str__(self):
#         return self.user.username
#
# # Модель отзыва
# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
#     comment = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Review for {self.product.name} by {self.customer.user.username}"
#
# # Модель заказа
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_paid = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"Order #{self.id} by {self.customer.user.username}"
#
# # Модель элемента заказа
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f"{self.product.name} ({self.quantity})"
#
# # Модель корзины
# class Cart(models.Model):
#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Cart of {self.customer.user.username}"
#
# # Модель элемента корзины
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#
#     def __str__(self):
#         return f"{self.product.name} ({self.quantity})"
# from django.db import models
#
# # Create your models here.
