from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Vacancy, Vacancy_resume, Resume, Volunteer


class VacancyListSerializer(ModelSerializer):
    type_work = serializers.StringRelatedField()
   
    class Meta:
        model = Vacancy
        fields = ('title', 'address', 'type_work','start_salary','end_salary', 'description')


class VacancyRetrieveSerializer(ModelSerializer):
    type_work = serializers.StringRelatedField()
    requirement = serializers.StringRelatedField(many=True)
    condition = serializers.StringRelatedField(many=True)

    class Meta:
        model = Vacancy
        fields = (
            'title', 
            'phone_number', 
            'address', 
            'type_work', 
            'start_salary', 
            'end_salary', 
            'salary_type', 
            'description', 
            'requirement', 
            'condition', 
            'views_count'
            )

class VacancyResumeCreateSerializer(ModelSerializer):

    class Meta:
        model = Vacancy_resume
        fields = ('vacancy_id', 'phone_number', 'resume_file')


class CreateResumeSerializer(ModelSerializer):

    class Meta:
        model = Resume
        fields = ('full_name', 'phone_number', 'file')


class CreateVolunteerSerializer(ModelSerializer):

    class Meta:
        model = Volunteer
        fields = ('full_name', 'email', 'phone_number', 'resume_file')