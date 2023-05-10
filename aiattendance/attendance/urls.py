from django.urls import path
from attendance import views

urlpatterns = [
    # path('', views.base, name='index'),
    path('', views.home, name='home'),
    path('attendpost/', views.attendpost, name='attendpost'),
    path('delete/', views.delete, name='delete'),
]