# Generated by Django 4.2.2 on 2023-09-13 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_studentsinfo_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsinfo',
            name='Date',
        ),
    ]
