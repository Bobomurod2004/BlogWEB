from rest_framework import generics
from app.serializers import *



class ArticleListAPIVew(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectList

    def get_queryset(self):
        return (
            Project.objects.all()
            .prefetch_related("technology_stack")
            # .select_related("some_fk")  # agar FK lar bo‘lsa
            .order_by("-create_at")
        )
