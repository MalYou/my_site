# Generated by Django 3.2.3 on 2021-05-16 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='capture',
            new_name='caption',
        ),
    ]
