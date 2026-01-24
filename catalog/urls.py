from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import home, contacts, products_list, products_detail

app_name = NewappConfig.name

urlpatterns = [
    path("", products_list, name="product_list"),
    path("products/<int:pk>/", products_detail, name="products_detail"),
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
]
