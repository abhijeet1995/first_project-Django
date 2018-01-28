from django import forms
from .models import Topic


class FormName(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

