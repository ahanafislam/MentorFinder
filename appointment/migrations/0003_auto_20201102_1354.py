# Generated by Django 2.2.13 on 2020-11-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20201101_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
