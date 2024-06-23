from django.shortcuts import render
from .models import Project
from .filters import TechFilter

# Create your views here.
def portfolio(request):
    filter = TechFilter(request.GET, queryset=Project.objects.all())

    return render(request, 'portfolio.html', { 'filter': filter})