# Generated by Django 2.0.2 on 2019-11-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0015_auto_20191129_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='static/images/default.png', null=True, upload_to='images'),
        ),
    ]