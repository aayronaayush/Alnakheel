# Generated by Django 2.2.10 on 2020-06-15 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200615_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('لقاء العدد', 'Interviews'), ('الفنون', 'Arts & Culture'), ('فيلم شاهدته', 'Film Reviews'), ('كتاب قرأته', 'Book Reviews'), ('رحلات وتجارب', 'Travel & Experience')], default='لقاء العدد', max_length=20),
        ),
    ]
