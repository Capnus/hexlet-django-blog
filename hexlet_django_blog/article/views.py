from django.http import HttpResponse
from hexlet_django_blog.views import IndexView

class IndexViewArticle(IndexView):

    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = 'Nickolas'
        return context
    