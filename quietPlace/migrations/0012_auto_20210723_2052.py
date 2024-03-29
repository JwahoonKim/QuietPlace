# Generated by Django 3.2.5 on 2021-07-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quietPlace', '0011_cafe_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='bathroom',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='booking_available',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='chair',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='discussion_room',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='place_size',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='socket',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='table',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='volume',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='wifi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
