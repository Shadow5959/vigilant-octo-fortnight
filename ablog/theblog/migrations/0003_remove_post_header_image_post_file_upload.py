# Generated by Django 5.0.1 on 2024-03-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_post_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='header_image',
        ),
        migrations.AddField(
            model_name='post',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
