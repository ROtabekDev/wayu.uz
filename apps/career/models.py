from django.db import models

from helpers.models import BaseModel


class Vacancy(BaseModel):
    """Bo`sh ish o`rinlari uchun model"""

    SALARY_TYPE = (
        ('Cash','Naqd'),
        ('Conversation','Suhbat orqali')
    )

    title = models.CharField('Nomi', max_length=150)
    phone_number = models.CharField('Telefon raqami', max_length=20)
    address = models.CharField('Manzili', max_length=250)
    type_work = models.ForeignKey('Work_type', on_delete=models.SET_NULL, null=True)
    start_salary = models.PositiveIntegerField('Boshlang`ich maosh', default=0, blank=True, null=True)
    end_salary = models.PositiveIntegerField('Eng yuqori maosh', default=0, blank=True, null=True)
    salary_type = models.CharField('Maosh turi', choices=SALARY_TYPE, max_length=20)
    description = models.TextField('Tavsifi')
    requirement = models.ManyToManyField('Requirement', verbose_name='Talab')
    condition = models.ManyToManyField('Condition', verbose_name='Shart')
    views_count = models.PositiveIntegerField('Ko`rishlar soni', default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Bo`sh ish o`rni'
        verbose_name_plural = 'Bo`sh ish o`rinlari'


class Work_type(BaseModel):
    """Ish turi"""
    name = models.CharField('Nomi', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ish turi'
        verbose_name_plural = 'Ish turlari'

    
class Requirement(BaseModel):
    """Talablar uchun model"""
    title = models.CharField('Nomi', max_length=150)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Talab'
        verbose_name_plural = 'Talablar'


class Condition(BaseModel):
    """Shartlar uchun model"""
    title = models.CharField('Nomi', max_length=150)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Shart'
        verbose_name_plural = 'Shartlar'

    
class Vacancy_resume(BaseModel):
    """Vakansiyadagi rezyumelar uchun model"""
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name='Vakansiya')
    phone_number = models.CharField('Telefon raqami', max_length=20)
    resume_file = models.FileField('Fayli', upload_to='career/vacancy_resume/files/')

    def __str__(self):
        return f"Vakansiya nomi : {self.vacancy_id.title} \n Nomzod telefon nomeri: {self.phone_number}"
        
    class Meta:
        verbose_name = 'Vakansiyadagi rezyume'
        verbose_name_plural = 'Vakansiyadagi rezyumelar'


class Resume(BaseModel):
    """Rezyumelar"""
    full_name = models.CharField('F.I.SH', max_length=150)
    phone_number = models.CharField('Telefon raqami', max_length=20)
    file = models.FileField('Fayl', upload_to='career/resume/files/')

    def __str__(self):
        return self.full_name
        
    class Meta:
        verbose_name = 'Rezyume'
        verbose_name_plural = 'Rezyumelar'


class Volunteer(BaseModel):
    """Volontyorlar uchun model"""
    full_name = models.CharField('F.I.SH', max_length=150)
    email = models.EmailField('Elektron pochta', max_length=100)
    phone_number = models.CharField('Telefon raqami', max_length=20)
    resume_file = models.FileField('Fayl', upload_to='career/volunteer/resume_file/')

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Volontyor'
        verbose_name_plural = 'Volontyorlar'


class Internship(BaseModel):
    """Amaliyot o`tash uchun nomzodlar modeli"""
    full_name = models.CharField('F.I.SH', max_length=150)
    email = models.EmailField('Elektron pochta', max_length=100)
    phone_number = models.CharField('Telefon raqami', max_length=20)
    address = models.CharField('Manzili', max_length=150)
    birthday = models.DateField('Tug`ilgan sanasi')
    business_area = models.CharField('Faoliyat sohasi', max_length=200)
    start_date = models.DateField('Boshlanish vaqti')
    work_type = models.ForeignKey(Work_type, on_delete=models.SET_NULL, null=True)
    education = models.CharField('O`qish joyi', max_length=150)
    speciality = models.CharField('Yo`nalishi', max_length=150)
    year_admission = models.DateField('Qabul qilingan yili')
    year_ending = models.DateField('Tugash yili')
    gpa = models.DecimalField('GPA', max_digits=3, decimal_places=2)
    experience = models.CharField('Tajriba', max_length=150)
    key_skills = models.CharField('Ko`nikmalari', max_length=150)
    resume = models.FileField('Rezyume fayli', upload_to='career/internship/resume_file/')

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Amaliyot o`tash uchun nomzod'
        verbose_name_plural = 'Amaliyot o`tash uchun nomzodlar'
