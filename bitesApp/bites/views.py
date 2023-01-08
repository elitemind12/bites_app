from django.shortcuts import render
from .models import Menu, Categorie
from django.views import generic
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import MenuSerializer, CategorieSerializer


'''........ class based built-in view for listing modal objects ......''' 

class HomeView(generic.ListView):

    template_name = 'bites/home.html'
    context_object_name = 'bites_list'

    def get_queryset(self):

        return Menu.objects.filter()

'''........ class based built-in view for view modal object ......''' 

class DetailView(generic.DetailView):

    model = Menu
    template_name = 'bites/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

'''........ class based built-in view for create modal object ......''' 

class CreateBites(generic.CreateView):
    model = Menu
    template_name = 'bites/new.html'
    fields = ['name','price','category','image']
    

'''........ class based built-in view for update modal object ......'''    
    
class UpdateBites(generic.UpdateView):
    model = Menu
    template_name = 'bites/update.html'
    fields = ['name','price','category','image']

'''........ class based built-in view for delete modal object ......'''

class DeleteBites(generic.DeleteView):
    model = Menu
    template_name = 'bites/delete.html'
    success_url = reverse_lazy('bites:home')


""" display bites modals as json """

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


    
    

