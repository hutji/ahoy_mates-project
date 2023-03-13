from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Главная страница'
    text = 'Это главная страница проекта Yatube'
    context = {
        'posts': posts,
        'title': title,
        'text': text,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    title = 'Информация о группах'
    text = 'Здесь будет главная информация о группах проекта'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'title': title,
        'posts': posts,
        'text': text,
    }
    
    return render(request, template, context)