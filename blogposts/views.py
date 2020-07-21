from django.shortcuts import render

from .models import Post, Category

# Create your views here.
def home(request):
    return render(request,'blogs/home.html')

def blogs(request, category):
    posts = Post.objects.get(category = category)
    return render(request, 'blogs/blogs.html', {'category': category, 'posts': posts})



