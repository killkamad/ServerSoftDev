from django.urls import path
from . import views

urlpatterns = [
    path('', views.com_list, name='com_list'),
    path('article/1', views.article, name='article'),
    path('article/1/art/<int:pk>/', views.com_detail, name='com_detail'),
    path('article/1/art/new/', views.com_new, name='com_new'),
    path('article/1/art/<int:pk>/edit/', views.com_edit, name='com_edit'),
    path('article/2', views.article2, name='article2'),
    path('article/2/art/<int:pk>/', views.com_detail2, name='com_detail2'),
    path('article/2/art/new/', views.com_new2, name='com_new2'),
    path('article/2/art/<int:pk>/edit/', views.com_edit2, name='com_edit2'),
    path('article/3', views.article3, name='article3'),
    path('article/3/art/<int:pk>/', views.com_detail3, name='com_detail3'),
    path('article/3/art/new/', views.com_new3, name='com_new3'),
    path('article/3/art/<int:pk>/edit/', views.com_edit3, name='com_edit3'),
]