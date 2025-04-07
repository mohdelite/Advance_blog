from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', dashboard_view, name='view'),
    path('dashboard/add_post/', add_post, name='add_post'),
    path('dashboard/edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('dashboard/delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('dashboard/manage_categories/', manage_categories, name='manage_categories'),
    path('dashboard/add_category/', add_category, name='add_category'),
    path('dashboard/edit_category/<int:category_id>/', edit_category, name='edit_category'),
    path('dashboard/delete_category/<int:category_id>/', delete_category, name='delete_category'),
    path('approve_comment/<int:comment_id>/', approve_comment, name='approve_comment'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    
]