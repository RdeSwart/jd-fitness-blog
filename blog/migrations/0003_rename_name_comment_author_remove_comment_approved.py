# Generated by Django 4.2.16 on 2024-12-09 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
    ]
