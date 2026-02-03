from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import NewappConfig
from catalog.views import (
    home,
    contacts,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCategoryListView,
)

app_name = NewappConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("category/<int:pk>/", cache_page(60)(ProductCategoryListView.as_view()), name="products_by_category"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="products_detail"),
    path("products/create", ProductCreateView.as_view(), name="products_create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"),
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
]
