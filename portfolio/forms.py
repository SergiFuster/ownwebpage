# forms.py
from django import forms
from .models import Technology

class TechnologyFilterForm(forms.Form):
    technologies = forms.ModelMultipleChoiceField(
        queryset=Technology.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
