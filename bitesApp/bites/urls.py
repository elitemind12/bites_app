from django.urls import path, include
from rest_framework import routers

from . import views

''' ........... register bites views to rest_framework router ...........'''
router = routers.DefaultRouter()
router.register(r'categories', views.CategorieViewSet)
router.register(r'menus', views.MenuViewSet)

'''........ paths to bites views ......''' 

app_name = 'bites'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), #... path to HomeView 
    path('new/', views.CreateBites.as_view(), name='new'), #... path to CreateBites view
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), #... path to DetailView
    path('<pk>/update', views.UpdateBites.as_view(), name='update'), #... path to UpdateBites view
    path('<pk>/delete', views.DeleteBites.as_view(), name='delete'), #... path to DeleteBites 
   #........... path to rest_framework router ...........
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
