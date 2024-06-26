from django.shortcuts import render
from .models import Project
from .forms import TechnologyFilterForm
from django.db.models import Count

# Create your views here.
def portfolio(request):
    form = TechnologyFilterForm(request.GET or None)
    projects = Project.objects.all()
    
    if form.is_valid():
        technologies = form.cleaned_data.get('technologies')
        if technologies:
            # Filtrar proyectos que contengan todas las tecnologías seleccionadas
            for tech in technologies:
                projects = projects.filter(technologies=tech)
            projects = projects.annotate(num_technologies=Count('technologies')).filter(num_technologies=len(technologies))
    
    return render(request, 'portfolio.html', {'form': form, 'projects': projects})