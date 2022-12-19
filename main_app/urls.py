from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('create/', views.create_post, name ='create'),
    path('edit/', views.edit, name ='edit'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]