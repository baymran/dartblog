from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>', SinglePost.as_view(), name='post'),
]