# Generated by Django 3.0.5 on 2021-06-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_contact_portfolio_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('mail', models.EmailField(blank=True, default='', max_length=100, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('message', models.TextField(blank=True, default='')),
                ('status', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='mail',
            field=models.EmailField(blank=True, default='', max_length=100, null=True),
        ),
    ]