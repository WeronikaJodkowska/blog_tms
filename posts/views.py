from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from posts.forms import PostForm
from posts.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def get_user_posts(request):
    author = request.user
    if author:
        posts = Post.objects.filter(author__exact=author)
    else:
        posts = Post.objects.all()
    return HttpResponse(", ".join([x.title for x in posts]))


def post_add(request):
    if not request.user.is_authenticated:
        return HttpResponse("You aren't authenticated!")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(author=request.user, **form.cleaned_data)
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post_add.html', {'form': form})