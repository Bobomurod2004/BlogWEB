from app.models import *
from rest_framework import serializers
from app.serializers.technology_stack_serializer import *

class ProjectList(serializers.ModelSerializer):
    create_at = serializers.SerializerMethodField()
    technology_stack = TechnologyStackList(many=True)
    class Meta:
        model = Project
        fields = ['title','description','project_image','status','git_link','link','technology_stack', 'create_at']

    def get_create_at(self, obj):
        return obj.create_at.strftime("%d-%m-%Y %H:%M:%S")

