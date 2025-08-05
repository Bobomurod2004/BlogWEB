from app.serializers import *
from . import views
from django.urls import path
urlpatterns = [
    path('list/', views.ArticleListAPIVew.as_view())
]