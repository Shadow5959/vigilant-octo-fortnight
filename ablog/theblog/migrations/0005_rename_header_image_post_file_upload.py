# Generated by Django 5.0.1 on 2024-03-20 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_rename_file_upload_post_header_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='header_image',
            new_name='FILE_UPLOAD',
        ),
    ]
