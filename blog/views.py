from django.shortcuts import render
from blog.models import Post
from blog.filters import PostFilter
# Create your views here.

def blog(request):
    filter = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, "blog.html", {"filter": filter, 'posts' : filter.qs})