from catalog.models import Product, Category

Category.objects.all().delete()
Product.objects.all().delete()
exit()
