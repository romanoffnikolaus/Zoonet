# Generated by Django 4.2 on 2023-05-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, primary_key=True, serialize=False),
        ),
    ]