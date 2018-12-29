from django.urls import path
from django.views.generic.base import RedirectView

from .views import (PostDetailView, PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserListView,
                    PostSearchView)

urlpatterns = [
    path('', RedirectView.as_view(url='/')),
    path('<str:username>/', UserListView.as_view(), name='user'),
    path('<int:pk>/post', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('create/newpost', PostCreateView.as_view(), name='create'),
    path('search/new', PostSearchView.as_view(), name='search')
]
