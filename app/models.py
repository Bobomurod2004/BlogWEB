from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    ARTICLE_CHOICES = [
        ('a joke',"Hazil"),
        ('information',"Ma'lumot"),
        ('fact',"Fakt")
    ]
    title = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=ARTICLE_CHOICES)

class Me(models.Model):
    image = models.ImageField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    git_link = models.URLField()
    linkedin_link = models.URLField()
    cv_file = models.FileField()
    resume = models.FileField()

class AboutMe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class TechnologyStack(models.Model):
    name = models.CharField(max_length=100, null=True ,blank=True)

class Project(models.Model):

    PROJECT_CHOICES = [
        ("code","Kod"),
        ("web_api","WEB API"),
        ('rest_api',"REST API"),
        ("fast_api","FAST API")
    ]

    create_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    project_image = models.ImageField()
    status = models.CharField(max_length=100, choices=PROJECT_CHOICES, null=True, blank=True)
    git_link = models.URLField()
    link = models.URLField()
    technology_stack = models.ManyToManyField(
        TechnologyStack, related_name='project_stack',

    )

class Skill(models.Model):
    key = models.CharField(max_length=100, null=True, blank=True)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.key} - {self.value}%"

class Comment(models.Model):
    full_name = models.CharField(max_length=100)
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now=True)

class Experience(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField()
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()