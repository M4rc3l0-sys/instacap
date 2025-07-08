from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from .models import Post

# Create your views here.
def index(request):
    return render(request,'index.html')

def posts(request):
    
    posts = Post.objects.all().select_related('user').prefetch_related('comments__user').order_by("-created_at")

    return render(request, 'posts/posts.html', {'posts': posts})


@login_required
def nuevo_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Asociamos el post al usuario logueado
            post.save()
            return redirect('/posts/')  # Redirige a la vista de inicio o de posts
    else:
        form = PostForm()
    return render(request, 'posts/nuevo_post.html', {'form': form})