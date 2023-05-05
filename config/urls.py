from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('main/', include('main.urls')),
    path('game/', include('game.urls')),
    path('end/', include('end.urls')),
    path('mvp/', include('mvp.urls')),



]
