# Generated by Django 3.0 on 2019-12-09 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATA', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='Nama_Chellenge',
            new_name='Nama_Lengkap',
        ),
    ]
