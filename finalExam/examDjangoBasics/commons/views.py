from django.views.generic import ListView, TemplateView
from examDjangoBasics.posts.models import Post


class DashboardView(ListView):
    model = Post
    template_name = 'dashboard.html'


class IndexView(TemplateView):
    template_name = 'index.html'
