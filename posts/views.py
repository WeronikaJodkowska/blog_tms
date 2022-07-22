from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post


def index(request):
    if request.GET.get('title'):
        post_list = Post.objects.filter(title__icontains=request.GET.get('title'))
    else:
        post_list = Post.objects.all()
    return HttpResponse(", ".join([x.title for x in post_list]))
