# Generated by Django 4.2.14 on 2024-07-18 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peer_to_peer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='riderprofile',
            old_name='phone',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='riderprofile',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='riderprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='riderprofile',
            name='source',
        ),
    ]
