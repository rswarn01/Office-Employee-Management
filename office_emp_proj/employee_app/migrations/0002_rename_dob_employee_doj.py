# Generated by Django 5.0.4 on 2024-04-04 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='dob',
            new_name='doj',
        ),
    ]
