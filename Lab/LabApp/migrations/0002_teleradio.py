# Generated by Django 5.0.2 on 2024-03-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LabApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeleRadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('designation', models.TextField()),
                ('city', models.TextField()),
            ],
        ),
    ]
