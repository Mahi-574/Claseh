from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Menu


# Create your views here.
class MenuList(ListView):
    queryset = Menu.objects.all()


class MenuDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Menu.objects.published(), slug=slug)

