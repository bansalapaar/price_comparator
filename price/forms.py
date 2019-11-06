from django import forms

class searching(forms.Form):
    search=forms.CharField(max_length=200,
    widget=forms.TextInput(attrs={'id':'mySearch','placeholder':'Search your product...'}))