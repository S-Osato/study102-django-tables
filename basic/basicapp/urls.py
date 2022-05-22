from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.CharactorCreate.as_view(), name='create'),
    path('list/', views.CharactorView.as_view(), name='list'),
]
