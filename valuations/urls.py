from django.urls import path
from . import views

urlpatterns = [
    path('', views.valuations_page, name='valuations_page'),
    path('add_valuations/', views.add_valuations, name='add_valuations')
]
