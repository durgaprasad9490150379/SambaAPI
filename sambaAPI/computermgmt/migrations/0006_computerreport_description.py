# Generated by Django 2.2.1 on 2019-12-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computermgmt', '0005_remove_computerreport_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='computerreport',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
