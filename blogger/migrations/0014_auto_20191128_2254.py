# Generated by Django 2.0.2 on 2019-11-28 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0013_auto_20191128_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsite',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
