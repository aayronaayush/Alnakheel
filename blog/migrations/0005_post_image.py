# Generated by Django 2.2.10 on 2020-06-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200323_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default='img/palm.png', upload_to=''),
        ),
    ]
