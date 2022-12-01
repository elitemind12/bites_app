from django.urls import path

from . import views

'''........ paths to bites views ......''' 

app_name = 'bites'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), #... path to HomeView 
    path('new/', views.CreateBites.as_view(), name='new'), #... path to CreateBites view
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), #... path to DetailView
    path('<pk>/update', views.UpdateBites.as_view(), name='update'), #... path to UpdateBites view
    path('<pk>/delete', views.DeleteBites.as_view(), name='delete') #... path to DeleteBites 
]
