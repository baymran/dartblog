from django.urls import path, include
from .views import *

urlpatterns = [
    path('', trees, name='trees'),
    path('elements/<int:pk>', get_elements, name='elements'),
]