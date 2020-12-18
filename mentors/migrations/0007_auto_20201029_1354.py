# Generated by Django 2.2.13 on 2020-10-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0006_auto_20201029_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='catagory',
            field=models.CharField(blank=True, choices=[('BUS', 'Business'), ('CAR', 'Career'), ('HNF', 'Health & Fitness'), ('LFS', 'Life Style'), ('PRD', 'Personal Development'), ('TNE', 'Teaching & Education')], default=None, max_length=300),
        ),
    ]