# Generated by Django 3.2.6 on 2021-08-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]