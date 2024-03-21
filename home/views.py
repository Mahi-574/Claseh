from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from menu.models import Menu
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, "home/index.html")


class SearchList(ListView):
    paginate_by = 10
    template_name = 'home/partials/search_list.html'

    def get_queryset(self):
        search = self.request.GET.get('strSearch')
        return Menu.objects.filter((Q(description__icontains=search) | Q(title__contains=search)))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('strSearch')
        return context


class SearchDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Menu.objects.published(), slug=slug)



