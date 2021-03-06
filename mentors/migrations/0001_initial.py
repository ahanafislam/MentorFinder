# Generated by Django 2.2.13 on 2020-10-27 00:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_by', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('professional_degree', models.CharField(max_length=200)),
                ('designation', models.CharField(blank=True, max_length=200)),
                ('specialist_in', models.CharField(blank=True, max_length=200)),
                ('visiting_houre', models.CharField(blank=True, max_length=200)),
                ('visiting_fees', models.CharField(max_length=200)),
                ('descriptions', models.TextField(blank=True)),
                ('sex', models.CharField(blank=True, max_length=50)),
                ('nid_no', models.CharField(blank=True, max_length=200)),
                ('catagory', models.CharField(blank=True, max_length=200)),
                ('chamber_address', models.CharField(blank=True, max_length=300)),
                ('district', models.CharField(blank=True, max_length=300)),
                ('divisions', models.CharField(blank=True, max_length=300)),
                ('mentors_picture', models.ImageField(blank=True, default='default.jpg', upload_to='photos/dp/mentors/%Y/%m/%d/')),
                ('cover_photo_1', models.ImageField(blank=True, default='default_cp.jpg', upload_to='photos/mentors/cover/%Y/%m/%d/')),
                ('cover_photo_2', models.ImageField(blank=True, upload_to='photos/mentors/cover/%Y/%m/%d/')),
                ('cover_photo_3', models.ImageField(blank=True, upload_to='photos/mentors/cover/%Y/%m/%d/')),
                ('join_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
                ('mentor_username', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
