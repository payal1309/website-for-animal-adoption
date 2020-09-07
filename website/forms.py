from django import forms
from .models import Accounts

class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields =['email','title','display','category','owner','address','number','desc','imageone']