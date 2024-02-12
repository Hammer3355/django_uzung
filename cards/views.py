from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Привет, мир!</h1>")

def catalog(request):
    return HttpResponse("<h1>Каталог карточек</h1>")

def get_card_by_id(request, card_id):
    return HttpResponse(f"<h1>Карточка по ID: {card_id}</h1>")


def get_category_by_name(request, slug):
    return HttpResponse(f"<h1>Категория {slug}</h1>")