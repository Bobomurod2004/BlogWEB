from app.models import *
from rest_framework import serializers

class ArticleListSerializer(serializers.ModelSerializer):
    create_at = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ['title','description','status','create_at']

    def get_create_at(self,obj):
        return obj.create_at.strftime("%d-%m-%Y %H:%M:%S")