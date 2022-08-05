from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

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
