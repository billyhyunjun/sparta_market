from django.urls import path
from . import views


app_name = "stores"
urlpatterns = [
    path('stores/', views.stores, name='stores'),
    path('stores_view/<int:pk>/', views.stores_view, name='stores_view'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
]

