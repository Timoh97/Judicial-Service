# Generated by Django 3.2.9 on 2022-08-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20220808_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]