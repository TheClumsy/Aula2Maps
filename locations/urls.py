from django.urls import path
from . import views

urlpatterns = [
    path('add_location/', views.add_location, name='add_location'),
    path('map/', views.map_page, name='map_page'),
    path('popup/', views.manage_popup, name='popup'),
    path('search/', views.search_page, name='search'),
    path('full_map/', views.show_full_map, name='map'),
]
