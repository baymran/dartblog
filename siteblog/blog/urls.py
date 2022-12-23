from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', get_categories, name='category'),
    path('post/<str:slug>', get_post, name='post')
]