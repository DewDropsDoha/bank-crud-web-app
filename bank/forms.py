from django import forms
from django.db.models import base
from django.forms import fields

from .models import Account

class AccountForm(forms.Form):
    balance   = forms.IntegerField(required=True)

class AccountModelForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = {"balance"}
