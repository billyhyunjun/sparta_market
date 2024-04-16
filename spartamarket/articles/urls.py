from django.urls import path
from . import views



app_name = "articles"
urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
    path('view/<int:pk>/', views.view, name='view'),
    path('like/<int:pk>/', views.like, name='like'),
    path('comment_create/<int:pk>/', views.comment_create, name='comment_create'),
    path('comment_delete/<int:pk>/', views.comment_delete, name='comment_delete'),
]

