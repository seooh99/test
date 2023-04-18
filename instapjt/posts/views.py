from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.

def index(req):
    
    return render(req, 'posts/index.html')


def create(req):
    if req.method == "POST":
        content = req.POST.get('content')
        post = Post(content = content)
        post.save()
        return redirect('posts:index')
    else:
        post = PostForm()
        context = {
            'post':post,
        }
        return render(req, 'posts/create.html', context)