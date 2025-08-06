from django.contrib import admin
from . import models

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    fields =['title', 'description', 'project_image','status', 'git_link', 'link' ,'technology_stack']

# admin.site.register(models.Project)
admin.site.register(models.TechnologyStack)
admin.site.register(models.Skill)
admin.site.register(models.Me)
admin.site.register(models.Article)
admin.site.register(models.AboutMe)
admin.site.register(models.Comment)
admin.site.register(models.Experience)

