# Generated by Django 2.0.2 on 2019-11-29 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0018_auto_20191129_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsite',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogger.Profile'),
        ),
    ]
