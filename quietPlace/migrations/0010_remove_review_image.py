# Generated by Django 3.2.5 on 2021-07-22 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quietPlace', '0009_alter_cafe_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
    ]
