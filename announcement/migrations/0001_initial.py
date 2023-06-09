# Generated by Django 4.2 on 2023-05-12 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('slug', models.SlugField(blank=True, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Иссык-куль', 'Иссык-куль'), ('Баткен', 'Баткен'), ('Талас', 'Талас'), ('Джалал-Абад', 'Джалал-Абад')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views_count', models.PositiveBigIntegerField(default=0)),
                ('phone_number', models.CharField(max_length=20)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='categories.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Announcements',
            },
        ),
        migrations.CreateModel(
            name='AnnouncementPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='announcementImages/')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcementImages', to='announcement.announcement')),
            ],
        ),
        migrations.AddIndex(
            model_name='announcementphoto',
            index=models.Index(fields=['announcement'], name='announcemen_announc_1e525d_idx'),
        ),
    ]
