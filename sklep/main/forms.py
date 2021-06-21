from django.db.models.fields import TextField
from django.forms.models import ModelForm
from .models import Comment
from django import forms

from django.contrib.auth import models
from django.forms import EmailField, fields, Textarea, widgets

from django.utils.translation import ugettext_lazy as _

from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist


class UserCreationForm(UserCreationForm):


    email = EmailField(label=_("Email address"), required=True,
        help_text=_("Required."))


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Taki użytkownik już istnieje")

    

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {
            'text': '',
        }
        

