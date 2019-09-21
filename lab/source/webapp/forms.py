from django import forms
from django.forms import widgets




class BookForm(forms.Form):
    name = forms.CharField(max_length=200, label='name', required=True)
    email = forms.EmailField(max_length=40, required=True,widget=widgets.EmailInput)
    text = forms.CharField(max_length=3000,  label='text', required=True,
                           widget=widgets.Textarea)


