# Generated by Django 3.2.5 on 2021-07-14 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quietPlace', '0003_auto_20210714_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cafe',
            old_name='location',
            new_name='address',
        ),
        migrations.AddField(
            model_name='cafe',
            name='category',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='region',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='bathroom',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='chair',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='discussion_room',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='franchise',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='place_size',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='socket',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='table',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='volume',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='wifi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='cafe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quietPlace.cafe'),
        ),
    ]
