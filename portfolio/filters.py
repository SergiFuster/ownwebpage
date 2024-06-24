from django import forms
from .models import Project,Technology
import django_filters

class TechFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['technologies']