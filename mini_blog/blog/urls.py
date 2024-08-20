from django.urls import path
from .views import PostlistCreate, PostRetrieveUpdateDestroy

urlpatterns = [
    path('posts/', PostlistCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post-detail'),
]