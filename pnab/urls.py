from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.reg, name='reg'),
    path('auth/', views.auth, name='auth'),
    path('home/', views.home, name='home'),
    path('logout/', views.logOut, name='logout'),
    path('add_statement/', views.add_statement, name='add_statement'),


    #Админка!!!!!
    path('admin1/', views.admin, name='admin'), #Админка!!!!!
    path('otvet/<int:statement_id>/', views.Otvet, name='otvet'),
    path('delete/<int:statement_id>/', views.Delete, name='delete')
    #Админка!!!!!


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
