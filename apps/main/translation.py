from modeltranslation.translator import register, TranslationOptions
from .models import (
    Management_staff, Admission_day, Employee_abroad, 
    Branch, Embasy, Consulate, Coordinator,
    Payment, Expense, Useful_links, Partner
)

@register(Management_staff)
class ManagementStaffTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'bio', 'tasks')


@register(Admission_day)
class AdmissionDayTranslationOptions(TranslationOptions):
    fields = ('start_day', 'end_day')


@register(Employee_abroad)
class EmployeeAbroadTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'tasks')


@register(Branch)
class BranchTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Embasy)
class EmbasyTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Consulate)
class ConsulateTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Coordinator)
class CoordinatorTranslationOptions(TranslationOptions):
    fields = ('title',)
  

@register(Payment)
class PaymentTranslationOptions(TranslationOptions):
    fields = ('full_name',)


@register(Expense)
class ExpenseTranslationOptions(TranslationOptions):
    fields = ('reason',)


@register(Useful_links)
class UsefulLinksTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('title', 'type')