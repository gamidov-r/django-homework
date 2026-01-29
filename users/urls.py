from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView
# from users.views import UserLoginView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(template_name="logout.html")),
    path("register/", UserCreateView.as_view(), name="register"),
]
