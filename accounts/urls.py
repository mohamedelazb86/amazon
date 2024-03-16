from django.urls import path
from .views import signup,activate

urlpatterns = [
    path('signup1',signup),
    path('<str:username>/activate',activate),
]
