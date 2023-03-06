from django.db import models

from helpers.models import BaseModel

from apps.main.models import Management_staff


class Project(BaseModel):
    """Loyihalar uchun model"""
    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)
    icon = models.ImageField('Rasmi', upload_to='projects/project/icon/')
    short_description = models.CharField('Qisqa tavsif', max_length=250)
    description = models.TextField('Tavsifi')
    video_link = models.URLField('Video uchun havola')
    team_members = models.ManyToManyField(Management_staff, verbose_name='Jamoa a`zolari')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Loyiha'
        verbose_name_plural = 'Loyihalar'


class Document_for_project(BaseModel):
    """Loyihalar uchun kerakli fayllar"""
    title = models.CharField('Nomi', max_length=150)
    type = models.ForeignKey('Document_type', on_delete=models.CASCADE)
    size = models.DecimalField('Hajmi', max_digits=7, decimal_places=3)
    file = models.FileField('Hujjat fayli', upload_to='projects/document/files/')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Loyiha')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Hujjat'
        verbose_name_plural = 'Hujjatlar'


class Document_type(BaseModel):
    """Hujjat turlari"""
    title = models.CharField('Nomi', max_length=150)
    icon = models.ImageField('Rasmi', upload_to='projects/document_type/icons/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Hujjat turi'
        verbose_name_plural = 'Hujjat turlari'


class Objective(BaseModel):
    """Loyihaning maqsadlari uchun model"""
    title = models.CharField('Nomi', max_length=100)
    icon = models.ImageField('Rasmi', upload_to='projects/objective/icons/')
    text = models.TextField('Maqsad matni')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Loyiha')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Loyiha uchun maqsad'
        verbose_name_plural = 'Loyiha uchun maqsadlar'



