import django_filters

from .models import Post

class PostSearch(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title':['icontains'],
            'content': ['icontains']
        }
