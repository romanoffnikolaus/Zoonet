# Generated by Django 4.2 on 2023-04-23 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=255)),
                ('adress_type', models.CharField(choices=[('hostel', 'Хостел/Приют'), ('clinic', 'Ветклиника'), ('zooshop', 'Зоомагазин'), ('babysitter', 'Зооняни')], max_length=50)),
                ('verified_adress', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='catalogImages')),
                ('phone_number', models.CharField(max_length=20)),
                ('location', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Иссык-куль', 'Иссык-куль'), ('Баткен', 'Баткен'), ('Талас', 'Талас'), ('Джалал-Абад', 'Джалал-Абад')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
