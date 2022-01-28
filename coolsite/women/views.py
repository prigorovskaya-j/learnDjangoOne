from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("Страница приложения women")

def categories(request, catId):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Страница {catId}</p>")

def main(request):
    return HttpResponse("<h1>Hello, Python</h1>")

def archive(request, year):
    if int(year)>2022:
        raise Http404()
    if int(year)<1999:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс. Страница не найдена</h1>')