from django.urls import path
from . import views



app_name = "articles"
urlpatterns = [
    path('about/', views.about, name='about'),
    path('articles/', views.articles, name='articles'),
    path('articles_view/<int:pk>/', views.articles_view, name='articles_view'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
    path('like/<int:pk>/', views.like, name='like'),
    path('like/articles/<int:pk>/', views.like_articles, name='like_articles'),
    path('comment_create/<int:pk>/', views.comment_create, name='comment_create'),
    path('comment_delete/<int:pk>/', views.comment_delete, name='comment_delete'),
    path('hashtag/<int:hash_pk>/', views.hashtag, name='hashtag'),
]

