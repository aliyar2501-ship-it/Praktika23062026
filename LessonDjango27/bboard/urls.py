from django.urls import path
from .views import TestPostClassView  # Импортируем наш класс

urlpatterns = [
    path('class-posts/', TestPostClassView.as_view(), name='test_class_post_api'),
]
