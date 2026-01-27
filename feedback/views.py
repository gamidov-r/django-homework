from django.shortcuts import render, get_object_or_404
from feedback.models import Feedback
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

### Feedback
class FeedbackListView(ListView):
    model = Feedback
    template_name = "feedback/entity_list.html"
    def get_queryset(self):
        return Feedback.objects.filter(published=True)


class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = "feedback/entity_detail.html"
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object

class FeedbackUpdateView(UpdateView):
    model = Feedback
    fields = ("title", "body", "preview", "created_at", "published", "view_counter")
    success_url = reverse_lazy("feedback:entity_list")
    template_name = "feedback/entity_form.html"
    def get_success_url(self):
        return reverse("feedback:entity_detail", args=(self.kwargs.get("pk"),))

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ("title", "body", "preview", "created_at", "published", "view_counter")
    success_url = reverse_lazy("feedback:entity_list")
    template_name = "feedback/entity_form.html"


class FeedbackDeleteView(DeleteView):
    model = Feedback
    success_url = reverse_lazy("feedback:entity_list")
    template_name = "feedback/entity_confirm_delete.html"

# ### catalog
#
# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"
#     def get_object(self, queryset=None):
#         self.object = super().get_object(queryset)
#         self.object.view_counter += 1
#         self.object.save()
#         return self.object
#
#
# class ProductCreateView(CreateView):
#     model = Product
#     fields = ("name", "value", "img", "created_at")
#     success_url = reverse_lazy("catalog:product_list")
#     template_name = "products/product_form.html"
#
#
# class ProductUpdateView(UpdateView):
#     model = Product
#     fields = ("name", "value", "img", "created_at")
#     success_url = reverse_lazy("catalog:product_list")
#     template_name = "products/product_form.html"
#     def get_success_url(self):
#         return reverse("catalog:products_detail", args=(self.kwargs.get("pk"),))
#
#
# class ProductDeleteView(DeleteView):
#     model = Product
#     success_url = reverse_lazy("catalog:product_list")
#     template_name = "products/product_confirm_delete.html"
#
#
# def home(request):
#     return render(request, "products/home.html")
#
#
# def contacts(request):
#     return render(request, "products/contacts.html")

# def products_list(request):
#     products = Product.objects.all()
#     context = {"object_list": products}
#     return render(request, "products/product_list.html", context)

# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "products/products_detail.html", context)



