from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('orders/', views.orders, name='orders'),
    path('place-order/', views.place_order, name='place_order'),  # ADD THIS LINE
]