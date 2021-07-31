from django import forms
from .models import *
class Purchaseform(forms.ModelForm):
    class Meta:
        model = POJ
        fields = "__all__"