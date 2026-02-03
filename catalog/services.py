from django.core.cache import cache

from config.settings import CACHE_ENABLED
from catalog.models import Product


def get_products_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_filter_products_by_category(category_for_filter):
    if not CACHE_ENABLED:
        return Product.objects.filter(category=category_for_filter)
    key = "category_list_"+str(category_for_filter)
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(category=category_for_filter)
    cache.set(key, products)
    return products

