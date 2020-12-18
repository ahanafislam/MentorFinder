# Generated by Django 2.2.13 on 2020-10-29 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0004_mentor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='district',
            field=models.CharField(blank=True, choices=[('BAR', 'Barisal'), ('CHI', 'Chittagong'), ('DHA', 'Dhaka'), ('KHU', 'Khulna'), ('MYM', 'Mymensingh'), ('RAJ', 'Rajshahi'), ('RAN', 'Rangpur'), ('SYL', 'Sylhet')], default=None, max_length=300),
        ),
    ]
