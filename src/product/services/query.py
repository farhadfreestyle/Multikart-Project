from django.db.models import QuerySet
from product.models import Product, Category, WriteReview
from django.db.models import Q


def date_price(created_at, price) -> QuerySet:
    return Product.objects.filter(created_at=created_at, price=price)


def category() -> QuerySet:
    return Category.objects.values_list('category', flat=True)


def last_eight() -> QuerySet:
    return Product.objects.all().order_by('-id')[:8]


def last_three() -> QuerySet:
    return Product.objects.all().order_by('-id')[:3]


def review(id) -> QuerySet:
    return WriteReview.objects.values_list('review_desc').filter(id=id)


def category_products(category) -> QuerySet:
    return Product.objects.values_list('name').filter(category=category)


def same_category(product) -> QuerySet:
    return Product.objects.filter(category=product.id)[:6]


def search(title, rating, color, category, brand, material) -> QuerySet:
    return Product.objects.filter(
        Q(title=title) | Q(rating=rating) | Q(color=color) | Q(category=category) | Q(brand=brand) | Q(
            material=material))