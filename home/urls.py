from django.urls import path
from .views import home, SearchList, SearchDetail

app_name = "home"
urlpatterns = [
    path('', home, name="home"),
    path('search/', SearchList.as_view(), name="search"),
    path('searchdetail/<slug:slug>', SearchDetail.as_view(), name="search_detail"),
]