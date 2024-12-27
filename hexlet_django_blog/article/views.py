from django.shortcuts import redirect, render
from django.urls import reverse
from hexlet_django_blog.views import IndexView

class IndexViewArticle(IndexView):

    template_name = 'articles/index.html'

    def index(self, request, tag, article_id):
        return render(
            request,
            'articles/index.html',
            context={
                'tag': tag,
                'article_id': article_id
            }
        )

    def home(self, request):
        return redirect(reverse('article', args=['python', 42]))
    