# Generated by Django 2.0.2 on 2019-11-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0019_auto_20191129_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='desig',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
