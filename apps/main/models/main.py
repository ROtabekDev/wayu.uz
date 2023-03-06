from django.db import models

from helpers.models import BaseModel

from apps.news.models import Country


class Management_staff(BaseModel):
    """Asosiy O`zbekistondagi hodimlar"""
    full_name = models.CharField('F.I.SH', max_length=150)
    profile_image = models.ImageField('Rasmi', upload_to='main/management_staff/images/')
    phone_number = models.CharField('Telefon nomeri', max_length=20)
    position = models.CharField('Lavozimi', max_length=150)
    email = models.EmailField('Elektron pochta', max_length=100)
    admission_day = models.ForeignKey('Admission_day', on_delete=models.SET_NULL, verbose_name='Qabul kunlari', null=True)
    bio = models.TextField('Biografiyasi')
    tasks = models.TextField('Vazifalari')

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Asosiy O`zbekistondagi hodim'
        verbose_name_plural = 'Asosiy O`zbekistondagi hodimlar'


class Admission_day(BaseModel):
    """Qabul kunlari uchun model"""

    WEEK_DAYS = (
        ('Monday', 'Dushanba'),
        ('Tuesday', 'Seshanba'),
        ('Wednesday', 'Chorshanba'),
        ('Thursday', 'Payshanba'),
        ('Friday', 'Juma'),
        ('Saturday', 'Shanba'),
        ('Sunday', 'Yakshanba'),
    )

    start_day = models.CharField('Boshlanish kuni', choices=WEEK_DAYS, default='Monday', max_length=20)
    end_day = models.CharField('Tigash kuni', choices=WEEK_DAYS, default='Friday', max_length=20)
    time_interval = models.CharField('Vaqt oralig`i', max_length=50)

    def __str__(self):
        return f"{self.start_day} dan {self.end_day} gacha. Soat {self.time_interval} oralig`ida."
    
    class Meta:
        verbose_name = 'Qabul kuni'
        verbose_name_plural = 'Qabul kunlari'


class Employee_abroad(BaseModel):
    """Chet eldagi xodimlar uchun model"""
    full_name = models.CharField('F.I.SH', max_length=150)
    profile_image = models.ImageField('Rasmi', upload_to='main/employee_abroad/images/')
    phone_number = models.CharField('Telefon nomeri', max_length=20)
    position = models.CharField('Lavozimi', max_length=150)
    email = models.EmailField('Elektron pochta', max_length=50)
    tasks = models.TextField('Vziflari')

    def ___str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Chet eldagi xodim'
        verbose_name_plural = 'Chet eldagi xodimlar'


class Branch(BaseModel):
    """Vakolatxonalar uchun model"""
    title = models.CharField('Nomi', max_length=150)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name = 'Mamlakati', null=True)
    employee_id = models.ForeignKey(Employee_abroad, on_delete=models.SET_NULL, verbose_name = 'Xodim', null=True)
    longitude = models.DecimalField('Uzunlik', max_digits=9, decimal_places=6)
    latitude = models.DecimalField('Kenglik', max_digits=9, decimal_places=6)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Vakolatxona'
        verbose_name_plural = 'Vakolatxonalar'


class Embasy(BaseModel):
    """Elchixonalar uchun model"""
    title = models.CharField('Nomi', max_length=150)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name = 'Mamlakati', null=True)
    employee_id = models.ForeignKey(Employee_abroad, on_delete=models.SET_NULL, verbose_name = 'Xodim', null=True)
    longitude = models.DecimalField('Uzunlik', max_digits=9, decimal_places=6)
    latitude = models.DecimalField('Kenglik', max_digits=9, decimal_places=6)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Elchixona'
        verbose_name_plural = 'Elchixonalar'


class Consulate(BaseModel):
    """Konsulliklar uchun model"""
    title = models.CharField('Nomi', max_length=150)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name = 'Mamlakati', null=True)
    employee_id = models.ForeignKey(Employee_abroad, on_delete=models.SET_NULL, verbose_name = 'Xodim', null=True)
    longitude = models.DecimalField('Uzunlik', max_digits=9, decimal_places=6)
    latitude = models.DecimalField('Kenglik', max_digits=9, decimal_places=6)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Konsullik'
        verbose_name_plural = 'Konsulliklar'


class Coordinator(BaseModel):
    """Koordinatorlar uchun model"""
    title = models.CharField('Nomi', max_length=150)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name = 'Mamlakati', null=True)
    employee_id = models.ForeignKey(Employee_abroad, on_delete=models.SET_NULL, verbose_name = 'Xodim', null=True)
    longitude = models.DecimalField('Uzunlik', max_digits=9, decimal_places=6)
    latitude = models.DecimalField('Kenglik', max_digits=9, decimal_places=6)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Koordinator'
        verbose_name_plural = 'Koordinatorlar'


