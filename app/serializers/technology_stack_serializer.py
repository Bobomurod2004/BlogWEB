from app.models import *
from rest_framework import serializers

class TechnologyStackList(serializers.ModelSerializer):
    class Meta:
        model = TechnologyStack
        fields = ['id', 'name']