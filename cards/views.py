from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


def index(request):
    """
    Возвращает рендер шаблона templates/cards/main.html
    """
    return render(request, 'cards/main.html')


def get_all_cards(request):
    """
    Возвращает все карточки для представления в каталоге
    """
    return HttpResponse('All cards')


def get_categories(request):
    """
    Возвращает все категории
    """
    return HttpResponse('All categories')


def get_cards_by_category(request, slug):
    """
    Возвращает все карточки по категории
    """
    return HttpResponse(f'All cards {slug}')


def get_cards_by_tag(request, slug):
    """
    Возвращает все карточки по тегу
    """
    return HttpResponse(f'Cards by tag {slug}')


def get_detail_card_by_id(request, card_id):
    """
    Возвращает детальную информацию по карточке
    """
    return HttpResponse(f'All {card_id}')
