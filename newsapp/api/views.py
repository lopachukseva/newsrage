from rest_framework.generics import ListAPIView, RetrieveAPIView

from newsapp.models import Category, News
from newsapp.api.serializers import CategorySerializer, NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsRetrieveAPIView(RetrieveAPIView):
    lookup_field = "slug"
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsCategoryAPIView(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.objects.filter(category__slug=self.kwargs["slug"])
        return queryset
