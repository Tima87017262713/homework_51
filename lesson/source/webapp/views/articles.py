from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def add_view(request: WSGIRequest):
    context = {'name': request.POST.get('name')}
    return render(request, 'article_create.html', context=context)
