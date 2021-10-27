from django.shortcuts import redirect, reverse
from django.views.generic import DetailView, ListView
from articles.models import Article


def index(request):
    return redirect(reverse('list_articles'))


class ArticleListView(ListView):
    model = Article
    paginate_by = 15

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'all')
        queryset = Article.objects.all()
        if filter_val != 'all':
            queryset = queryset.filter(category=filter_val)
        return queryset.order_by('title')


class ArticlesView(DetailView):
    model = Article
