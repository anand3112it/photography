# Generated by Django 3.2.6 on 2021-08-20 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0004_auto_20210820_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='created_date',
            field=models.DateField(null=True),
        ),
    ]