from django import forms 
from .models import DressVerity


class DressVerityForm(forms.Form):
    dress_verity = forms.ModelChoiceField(queryset=DressVerity.objects.all(),label="Select Dress Variety")