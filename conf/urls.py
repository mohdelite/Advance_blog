
from django.contrib import admin
from django.urls import path, include
from .views import index_view, search, user_login, user_logout

urlpatterns = [
    path('search/', search, name='search_results'),
    path('', index_view, name='home'),
    path('login/', user_login, name='login_page'),
    path('logout/', user_logout, name='logout'),
]