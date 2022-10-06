from django.urls import path
from .views import Create


urlpatterns = [
    path('a/', Create.as_view()),
]