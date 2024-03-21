from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Page


# Create your views here.
class PageDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Page.objects.all(), slug=slug)

