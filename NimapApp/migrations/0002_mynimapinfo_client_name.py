# Generated by Django 4.0.6 on 2022-07-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NimapApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mynimapinfo',
            name='client_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]