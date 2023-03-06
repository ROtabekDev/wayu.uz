from django.contrib import admin

from .models import (
    Management_staff,
    Employee_abroad,
    Admission_day,
    Branch,
    Embasy,
    Consulate,
    Coordinator,
    Message,
    Expense,
    Useful_links,
    Payment,
    Partner
)


@admin.register(Management_staff)
class ManagementStaffModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'position')


@admin.register(Admission_day)
class AdmissionDayModelAdmin(admin.ModelAdmin):
    list_display = ('start_day', 'end_day', 'time_interval')


@admin.register(Employee_abroad)
class EmployeeAbroadModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'position')


@admin.register(Branch)
class BranchModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_country', 'get_employee')

    def get_country(self, obj):
        return obj.country_id.name
    
    def get_employee(self, obj):
        return obj.employee_id.ful_name

@admin.register(Embasy)
class EmbasyModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_country', 'get_employee')

    def get_country(self, obj):
        return obj.country_id.name
    
    def get_employee(self, obj):
        return obj.employee_id.ful_name


@admin.register(Consulate)
class ConsulateModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_country', 'get_employee')

    def get_country(self, obj):
        return obj.country_id.name
    
    def get_employee(self, obj):
        return obj.employee_id.ful_name


@admin.register(Coordinator)
class CoordinatorModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_country', 'get_employee')

    def get_country(self, obj):
        return obj.country_id.name
    
    def get_employee(self, obj):
        return obj.employee_id.ful_name


@admin.register(Message)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email')


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'amount')


@admin.register(Expense)
class ExpenseModelAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'reason')


@admin.register(Useful_links)
class UsefulLinksModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')


@admin.register(Partner)
class PartnerModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'type')






