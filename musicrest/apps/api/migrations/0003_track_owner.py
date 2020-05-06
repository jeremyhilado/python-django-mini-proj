# Generated by Django 3.0.6 on 2020-05-06 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('api', '0002_album_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.User'),
            preserve_default=False,
        ),
    ]