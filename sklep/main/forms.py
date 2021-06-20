from django.forms.models import ModelForm
from .models import Comment
from django import forms
from django.contrib.auth import models
from django.forms import EmailField, fields

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True,
        help_text=_("Required."))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CommentForm(ModelForm):


    class Meta:
        model = Comment
        fields = ['user', 'movie', 'text']

