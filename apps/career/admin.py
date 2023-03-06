from django.contrib import admin

from .models import (
        Vacancy, 
        Work_type, 
        Requirement, 
        Condition,
        Vacancy_resume,
        Resume,
        Volunteer, 
        Internship
    )


@admin.register(Vacancy)
class VacancyModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone_number', 'address')


@admin.register(Work_type)
class WorkTypeModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Requirement)
class RequirementModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Condition)
class ConditionModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Vacancy_resume)
class VacancyResumeModelAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)


@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')


@admin.register(Volunteer)
class VolunteerModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')


@admin.register(Internship)
class InternshipModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')