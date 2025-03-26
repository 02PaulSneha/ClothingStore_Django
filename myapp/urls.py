
from django.urls import path
from . import views 

urlpatterns = [
  
    path('', views.all_myapp, name='all_myapp'),
    path('<int:dress_id>/', views.dress_detail, name='dress_detail'),
    path('dress_store/', views.dress_store_view, name='dress_store'),
    
    ]