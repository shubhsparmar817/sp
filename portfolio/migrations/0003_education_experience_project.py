# Generated by Django 3.0.5 on 2021-06-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('start', models.IntegerField(blank=True, default='', null=True)),
                ('end', models.IntegerField(blank=True, default='', null=True)),
                ('college', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('percentage', models.IntegerField(blank=True, default='', null=True)),
                ('percentageType', models.CharField(blank=True, default='', max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('employmentType', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('start', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('end', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('company', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('location', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('website', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('desc1', models.TextField(default='')),
                ('desc2', models.TextField(default='')),
                ('desc3', models.TextField(default='')),
                ('desc4', models.TextField(default='')),
                ('desc5', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('desc', models.TextField(default='')),
            ],
        ),
    ]
