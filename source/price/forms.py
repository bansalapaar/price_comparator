"""
it is search bar for our website created using django
"""
from django import forms

class searching(forms.Form):
    search=forms.CharField(max_length=200,
    widget=forms.TextInput(attrs={'class':'form-control','id':'txtSearch','placeholder':'Search your product...'}))
