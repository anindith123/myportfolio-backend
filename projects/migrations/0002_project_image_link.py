# Generated by Django 2.1.3 on 2018-12-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_link',
            field=models.URLField(default='#'),
        ),
    ]
