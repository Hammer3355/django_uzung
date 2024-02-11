from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Привет, мир!</h1>")


def catalog(request):
    return HttpResponse("<h1>Каталог карточек</h1>")