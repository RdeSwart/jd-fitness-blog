# Generated by Django 4.2.16 on 2024-12-16 20:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_blogpost_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blogpost_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
