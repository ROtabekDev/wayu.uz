from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import (
    Management_staff, Admission_day, Employee_abroad, 
    Branch, Embasy, Consulate, Coordinator
    )

from apps.news.serializers import CountrySerializer

class AdmissionDaySerializer(ModelSerializer):

    class Meta:
        model = Admission_day
        fields = ('start_day', 'end_day', 'time_interval')


class ManagementStaffSerializer(ModelSerializer):
    admission_day = AdmissionDaySerializer()

    class Meta:
        model = Management_staff
        fields = ('full_name', 'profile_image', 'phone_number', 'position', 'email', 'admission_day', 'bio', 'tasks')


class EmployeeAbroadSerializer(ModelSerializer):

    class Meta:
        model = Employee_abroad
        fields = ('full_name', 'profile_image', 'phone_number', 'position', 'email', 'tasks')

class BranchSerializer(ModelSerializer):
    country_id = CountrySerializer()
    employee_id = EmployeeAbroadSerializer()

    class Meta:
        model = Branch
        fields = ('title', 'country_id', 'employee_id')