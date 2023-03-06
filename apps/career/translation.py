from modeltranslation.translator import register, TranslationOptions
from .models import (
    Vacancy, Work_type, Requirement, 
    Condition, Volunteer
)

@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'address', 'salary_type', 'description')


@register(Work_type)
class WorkTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Requirement)
class RequirementTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Condition)
class ConditionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Volunteer)
class VolunteerTranslationOptions(TranslationOptions):
    fields = ('full_name',)