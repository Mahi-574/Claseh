from django.urls import path
from .views import PageDetail

app_name = "pages"
urlpatterns = [
    path('', PageDetail.as_view(), name="pages")
]