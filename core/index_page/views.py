from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin

# Create your views here.


class IndexPageView(TemplateView, ContextMixin):
    """
    Класс представления для основной страницы
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
