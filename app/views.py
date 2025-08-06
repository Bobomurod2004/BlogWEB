from rest_framework import generics
from app.serializers import *


class ArticleListAPIVew(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectList
