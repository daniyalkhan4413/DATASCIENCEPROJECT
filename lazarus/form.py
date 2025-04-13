from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User


class myusercreationform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','name', 'email', 'password1', 'password2']


class Userform(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name' , 'bio']
