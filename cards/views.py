from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request

"""
index - возвращает главную страницу - шаблон /templates/cards/main.html
about - возвращает страницу "О проекте" - шаблон /templates/cards/about.html
catalog - возвращает страницу "Каталог" - шаблон /templates/cards/catalog.html


get_categories - возвращает все категории для представления в каталоге
get_cards_by_category - возвращает карточки по категории для представления в каталоге
get_cards_by_tag - возвращает карточки по тегу для представления в каталоге
get_detail_card_by_id - возвращает детальную информацию по карточке для представления

render(запрос, шаблон, контекст=None)
    Возвращает объект HttpResponse с отрендеренным шаблоном шаблон и контекстом контекст.
    Если контекст не передан, используется пустой словарь.
"""

about_info = {
    'users_count': 100500,
    'cards_count': 200600
}

def index(request):
    """
    Возвращает рендер шаблона templates/cards/main.html
    """
    return render(request, 'cards/main.html')


def about(request):
    return render(request, 'cards/about.html', context=about_info)


def catalog(request):
    return render(request, 'cards/catalog.html')



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
