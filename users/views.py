from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.views.generic import CreateView
from users.forms import UserRegisterForm
from django.urls import reverse_lazy
from users.models import User
from config.settings import EMAIL_HOST_USER

# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")
    template_name = "users/login.html"

    def form_valid(self, form):
        user = form.save()
        # user.is_active = False
        send_mail(
            subject="Приветствуем на нашем сайте!",
            message=f"Привет, {user.email}!\nСпасибо за регистрацию на нашем сайте.\nТеперь ты можешь не только смотреть список продуктов, но и открывать каждый из них, внося изменения!",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        user.owner = user
        return super().form_valid(form)


class UserLoginView(LoginView):
    model = User
    form_class = AuthenticationForm
    template_name = "users/login.html"
    success_url = reverse_lazy("catalog:product_list")


class DUserLogoutView(LogoutView):
    model = User
    template_name = "users/logout.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = form.save()


class UserLogoutView(LogoutView):
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == "get":
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
