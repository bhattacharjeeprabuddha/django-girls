# Generated by Django 3.2.25 on 2024-06-01 05:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(null=True, verbose_name=django.utils.timezone.now),
        ),
    ]
