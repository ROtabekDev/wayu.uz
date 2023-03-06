from django.contrib import admin

from .models import Project, Document_for_project, Document_type, Objective


@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')


@admin.register(Document_for_project)
class DocumentForProjectModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'size')


@admin.register(Document_type)
class DocumentTypeModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Objective)
class ObjectiveModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
