# Generated by Django 3.1 on 2021-10-03 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20211003_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rango.category'),
        ),
    ]