# Generated by Django 5.1.4 on 2025-01-17 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='ip_adress',
            new_name='ip_address',
        ),
    ]
