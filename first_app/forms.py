from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    about_me = forms.CharField(widget=forms.Textarea)
