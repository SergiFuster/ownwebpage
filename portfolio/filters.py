from django import forms
from .models import Project
import django_filters

class TechFilter(django_filters.FilterSet):
    technology = django_filters.ModelMultipleChoiceFilter(queryset=Project.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Project
        fields = ['technologies']