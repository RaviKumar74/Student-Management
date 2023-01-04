from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('all_stu', views.all_stu, name='all_stu'),
    path('add_stu', views.add_stu, name='add_stu'),
    path('remove_stu', views.remove_stu, name='remove_stu'),
    path('remove_stu/<int:stu_id>', views.remove_stu, name='remove_stu'),
    path('login/',loginAPI.as_view())
    # path('filter_stu', views.filter_stu, name='filter_stu'),
]