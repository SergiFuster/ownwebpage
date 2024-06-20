from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    list_filter = ['date_posted']
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)