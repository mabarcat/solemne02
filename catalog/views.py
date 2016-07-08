from django.shortcuts import render

from catalog.models import Category, Product, Trademark

def category(request,category_id):

    products = Product.objects.filter(category__id=category_id)

    return render(request, 'category.html', {'products':products})