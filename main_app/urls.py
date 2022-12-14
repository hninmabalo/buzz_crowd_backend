from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('create/', views.create_post, name ='create'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('like/', views.like_post, name ='like'),
    path('edit/', views.edit, name ='edit'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]