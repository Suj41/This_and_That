# Generated by Django 5.0.1 on 2024-02-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_bilingsystem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilingsystem',
            name='transaction_id',
            field=models.IntegerField(default='1000'),
        ),
    ]
