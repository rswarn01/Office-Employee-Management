# Generated by Django 5.0.4 on 2024-04-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_rename_dob_employee_doj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateField(auto_now=True),
        ),
    ]