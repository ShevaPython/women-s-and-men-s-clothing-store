from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def index(request):
    return render(request, 'shop/index_shop.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(stock=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
    products = products.filter(category=category)
    return render(request,
                  'shop/index_shop.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                stock=True)
    return render(request,
                  'shop/index_shop.html',
                  {'product': product})
