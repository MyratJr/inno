# Generated by Django 5.0.6 on 2024-10-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nis_app', '0009_rename_description_innovationpractice_description_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovationpractice',
            name='description_ja',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='innovationpractice',
            name='description_tk',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
