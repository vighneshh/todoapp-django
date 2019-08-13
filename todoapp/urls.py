from django.urls import path, include
from .views import ToDoView
from . import views
urlpatterns = [
    
    path('',ToDoView.as_view(),name='todo'),
    path('completed/<pk>/', views.Completed, name='completed'),
    path('deletecompleted', views.DeleteCompleted, name='deletecompleted'),
    path('deleteall', views.DeleteAll, name='deleteall')
]

