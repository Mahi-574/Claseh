from django.urls import path
from .views import MenuList, MenuDetail

app_name = "menu"
urlpatterns = [
    path('', MenuList.as_view(), name="menu"),
    path('menu-datail/<slug:slug>', MenuDetail.as_view(), name="detail"),
]