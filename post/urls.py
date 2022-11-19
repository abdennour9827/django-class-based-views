from django.contrib import admin
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list),
    path('<int:year>/', views.pos_detail),
]
