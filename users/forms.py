from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)  # We only specify the email address, the password is the default one.


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'country', 'avatar')
