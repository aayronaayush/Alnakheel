# Generated by Django 2.2.10 on 2020-09-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200615_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
