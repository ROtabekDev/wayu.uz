# Generated by Django 4.1.7 on 2023-03-06 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('start_day', models.CharField(choices=[('Monday', 'Dushanba'), ('Tuesday', 'Seshanba'), ('Wednesday', 'Chorshanba'), ('Thursday', 'Payshanba'), ('Friday', 'Juma'), ('Saturday', 'Shanba'), ('Sunday', 'Yakshanba')], default='Monday', max_length=20, verbose_name='Boshlanish kuni')),
                ('end_day', models.CharField(choices=[('Monday', 'Dushanba'), ('Tuesday', 'Seshanba'), ('Wednesday', 'Chorshanba'), ('Thursday', 'Payshanba'), ('Friday', 'Juma'), ('Saturday', 'Shanba'), ('Sunday', 'Yakshanba')], default='Friday', max_length=20, verbose_name='Tigash kuni')),
                ('time_interval', models.CharField(max_length=50, verbose_name='Vaqt oralig`i')),
            ],
            options={
                'verbose_name': 'Qabul kuni',
                'verbose_name_plural': 'Qabul kunlari',
            },
        ),
        migrations.CreateModel(
            name='Employee_abroad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('full_name', models.CharField(max_length=150, verbose_name='F.I.SH')),
                ('profile_image', models.ImageField(upload_to='main/employee_abroad/images/', verbose_name='Rasmi')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefon nomeri')),
                ('position', models.CharField(max_length=150, verbose_name='Lavozimi')),
                ('email', models.EmailField(max_length=50, verbose_name='Elektron pochta')),
                ('tasks', models.TextField(verbose_name='Vziflari')),
            ],
            options={
                'verbose_name': 'Chet eldagi xodim',
                'verbose_name_plural': 'Chet eldagi xodimlar',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Pul miqdori')),
                ('date', models.DateTimeField(verbose_name='Sanasi')),
                ('reason', models.CharField(max_length=150, verbose_name='Sababi')),
                ('report', models.FileField(upload_to='', verbose_name='Hisoboti')),
            ],
            options={
                'verbose_name': 'Xarajat',
                'verbose_name_plural': 'Xarajatlar',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('full_name', models.CharField(max_length=100, verbose_name='Ism, familiya')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefon raqam')),
                ('email', models.EmailField(max_length=50, verbose_name='Elektron pochta')),
                ('text', models.TextField(verbose_name='Xabar')),
            ],
            options={
                'verbose_name': 'Xabar',
                'verbose_name_plural': 'Xabarlar',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('icon', models.ImageField(upload_to='main/partner/icon/', verbose_name='Rasmi')),
                ('link', models.URLField(max_length=150, verbose_name='Link')),
                ('type', models.CharField(choices=[('State', 'Davlat'), ('Own', 'Xususiy')], max_length=20, verbose_name='Homiy turi')),
            ],
            options={
                'verbose_name': 'Hamkor',
                'verbose_name_plural': 'Hamkorlar',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('full_name', models.CharField(max_length=100, verbose_name='Ism, familiya')),
                ('date', models.DateTimeField(verbose_name='Sanasi')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Pul miqdori')),
            ],
            options={
                'verbose_name': 'To`lov',
                'verbose_name_plural': 'To`lovlar',
            },
        ),
        migrations.CreateModel(
            name='Useful_links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('icon', models.ImageField(upload_to='main/useful_link/icon', verbose_name='Rasmi')),
                ('link', models.URLField(max_length=150, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Foydali havola',
                'verbose_name_plural': 'Foydali havolalar',
            },
        ),
        migrations.CreateModel(
            name='Management_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('full_name', models.CharField(max_length=150, verbose_name='F.I.SH')),
                ('profile_image', models.ImageField(upload_to='main/management_staff/images/', verbose_name='Rasmi')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefon nomeri')),
                ('position', models.CharField(max_length=150, verbose_name='Lavozimi')),
                ('email', models.EmailField(max_length=100, verbose_name='Elektron pochta')),
                ('bio', models.TextField(verbose_name='Biografiyasi')),
                ('tasks', models.TextField(verbose_name='Vazifalari')),
                ('admission_day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.admission_day', verbose_name='Qabul kunlari')),
            ],
            options={
                'verbose_name': 'Asosiy O`zbekistondagi hodim',
                'verbose_name_plural': 'Asosiy O`zbekistondagi hodimlar',
            },
        ),
        migrations.CreateModel(
            name='Embasy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Uzunlik')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Kenglik')),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.country', verbose_name='Mamlakati')),
                ('employee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.employee_abroad', verbose_name='Xodim')),
            ],
            options={
                'verbose_name': 'Elchi',
                'verbose_name_plural': 'Elchilar',
            },
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Uzunlik')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Kenglik')),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.country', verbose_name='Mamlakati')),
                ('employee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.employee_abroad', verbose_name='Xodim')),
            ],
            options={
                'verbose_name': 'Koordinator',
                'verbose_name_plural': 'Koordinatorlar',
            },
        ),
        migrations.CreateModel(
            name='Consulate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Uzunlik')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Kenglik')),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.country', verbose_name='Mamlakati')),
                ('employee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.employee_abroad', verbose_name='Xodim')),
            ],
            options={
                'verbose_name': 'Konsullik',
                'verbose_name_plural': 'Konsulliklar',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Uzunlik')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Kenglik')),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.country', verbose_name='Mamlakati')),
                ('employee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.employee_abroad', verbose_name='Xodim')),
            ],
            options={
                'verbose_name': 'Vakolatxona',
                'verbose_name_plural': 'Vakolatxonalar',
            },
        ),
    ]
