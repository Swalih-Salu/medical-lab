# Generated by Django 5.0.2 on 2024-03-20 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bkapmt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('number', models.IntegerField()),
                ('city', models.TextField()),
            ],
        ),
    ]