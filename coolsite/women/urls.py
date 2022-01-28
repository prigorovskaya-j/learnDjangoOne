from django.urls import path
from django.urls import re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catId>/', categories),  # http://127.0.8.1:8000/women/cats/1/
    path('main/', main),
    re_path(r'^archive/(?P<year>[0-9]{4})', archive),
]