from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('about/', views.about),
    path('admin/', admin.site.urls),
]
