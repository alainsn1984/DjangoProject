from django.urls import path
from .views import index, like


urlpatterns = [
    path('', index, name='index'),
    path('like/', like, name='like'),
]