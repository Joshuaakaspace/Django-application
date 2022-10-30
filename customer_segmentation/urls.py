from django.urls import path
from . import views
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = "login" ),
    path('logout/', views.signout, name = "logout" ),
    path('home/', views.home1, name="home"),
    path('updateaccount/<int:id>', views.update_account, name="update_account"),
    path('updateunsegmented/', views.update_unsegmented, name="update_unsegmented"),
    path('updateurl/', views.update_url, name="update_url"),
    path('searchexisting/', views.search_existing, name="search_existing"),
    path('loadfile/', views.loadFile, name="loadFile"),
    
] 
