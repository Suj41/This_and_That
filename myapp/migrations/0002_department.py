# Generated by Django 5.0.1 on 2024-02-20 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(max_length=50)),
                ('depttype', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('appuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.appuser')),
            ],
        ),
    ]
