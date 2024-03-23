# Generated by Django 4.1.4 on 2024-03-18 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('nurse', 'Nurse'), ('doctor', 'Doctor'), ('patient', 'Patient'), ('admin', 'Admin')], max_length=50),
        ),
    ]
