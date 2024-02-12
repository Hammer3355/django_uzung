from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    # Карточки по ID
    path('catalog/<int:card_id>/', views.get_card_by_id, name='card'),
    # Карточки по slug
    path('catalog/<slug:slug>', views.get_category_by_name, name='category'),
]