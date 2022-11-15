from django.shortcuts import render 
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Страница, на которой будут, отфильтрованные авто по другим закупкам {slug}')
