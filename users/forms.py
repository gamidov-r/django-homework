from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormProduct
from users.models import User

class UserRegisterForm(StyleFormProduct, UserCreationForm):
    class Meta:
        model = User
        exclude = ("view_counter",)
        fields = ("email","password1","password2")




