# Generated by Django 5.0.6 on 2024-10-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nis_app', '0003_alter_country_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=55)),
                ('gmail', models.CharField(max_length=55)),
                ('title', models.CharField(max_length=55)),
                ('desc', models.TextField()),
            ],
        ),
    ]
