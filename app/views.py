from rest_framework import generics
from app.serializers import *


class ArticleListAPIVew(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

