# Generated by Django 2.2.10 on 2020-03-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200213_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isCurrentFeature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='isFeature1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='isFeature2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='isFeature3',
            field=models.BooleanField(default=False),
        ),
    ]
