from django.shortcuts import render
from blog.models import Post
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    print("Rendering blog.html")
    return render(request, "blog.html", {"posts": posts})