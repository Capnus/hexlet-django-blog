from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexView(TemplateView):

    template_name = 'index.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'THE WORLDO'
        return context


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )
