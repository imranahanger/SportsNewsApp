from django import forms

class KeyForm(forms.Form):
    key = forms.CharField(max_length=255,
    widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your Key here'}))