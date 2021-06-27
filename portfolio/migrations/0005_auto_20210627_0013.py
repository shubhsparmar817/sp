# Generated by Django 3.0.5 on 2021-06-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_education_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='location',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='university',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]