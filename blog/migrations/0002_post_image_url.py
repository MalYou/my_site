# Generated by Django 3.2.3 on 2021-05-15 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
