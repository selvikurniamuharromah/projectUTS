# Generated by Django 4.1.2 on 2022-10-16 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soal', '0002_guru'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GURU',
            new_name='mahasiswa',
        ),
        migrations.RenameField(
            model_name='mahasiswa',
            old_name='NIP',
            new_name='NIM',
        ),
    ]
