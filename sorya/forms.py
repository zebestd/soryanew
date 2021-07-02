from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import *



class SoruForm(ModelForm):
    class Meta:
         model = Soru
         fields = ('isim', 'kategori', 'soru')

class YanitForm(forms.ModelForm):
    class Meta:
        model = Yanit
        fields = ('text',)