from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexViewArticle

urlpatterns = [
    path(
        '<str:tags>/<int:author_id>/',
        IndexViewArticle.as_view(),
        name='article'
    ),
    
]
