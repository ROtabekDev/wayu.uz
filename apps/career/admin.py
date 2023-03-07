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
    list_display_links = ('title',)
    list_filter = ('type_work',)


@admin.register(Work_type)
class WorkTypeModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',) 

@admin.register(Requirement)
class RequirementModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',) 


@admin.register(Condition)
class ConditionModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',) 


@admin.register(Vacancy_resume)
class VacancyResumeModelAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
    list_display_links = ('phone_number',)
    list_filter = ("vacancy_id",) 

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')
    list_display_links = ('full_name', ) 

@admin.register(Volunteer)
class VolunteerModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')
    list_display_links = ('full_name', 'email') 

@admin.register(Internship)
class InternshipModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')
    list_display_links = ('full_name', 'email') 