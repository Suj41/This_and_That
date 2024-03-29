# Generated by Django 5.0.1 on 2024-02-28 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='BilingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField(max_length=25)),
                ('contact', models.CharField(max_length=25)),
                ('product', models.CharField(max_length=250)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.productcategory')),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
            ],
        ),
    ]
