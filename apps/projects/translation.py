from modeltranslation.translator import register, TranslationOptions
from .models import (
    Project, Document_for_project, Document_type, 
    Objective
)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')


@register(Document_for_project)
class DocumentForProjectTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Document_type)
class DocumentTypeTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Objective)
class ObjectiveTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

 