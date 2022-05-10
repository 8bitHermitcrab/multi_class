# 여러 url들 관리

from django.urls import path
from . import views

# Routing
urlpatterns = [
    path('', views.index, name='index'),
]