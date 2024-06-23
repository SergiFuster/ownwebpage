from django.contrib import admin
from .models import Project, Link, Technology

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Link)
admin.site.register(Technology)