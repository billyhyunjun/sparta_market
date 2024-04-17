from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('follow/<int:user_id>', views.follow, name='follow'),
    path('gatcha/', views.gatcha, name='gatcha'),
    path('cards/<int:pk>', views.cards, name='cards'),
]
