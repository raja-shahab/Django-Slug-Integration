from django.contrib import admin
from django.urls import path
from slug_intergration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<slug:slug>/', views.post, name='blog')
]
