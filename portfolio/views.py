from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Portfolio
from django.shortcuts import get_object_or_404


# Create your views here.
class PortfolioList(ListView):
    queryset = Portfolio.objects.all()


class PortfolioDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Portfolio.objects.all(), slug=slug)