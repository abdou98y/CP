# Generated by Django 5.1 on 2024-08-28 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_protofolio', '0019_remove_projectpagegallery_gallery_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='facities',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='gallery_images',
        ),
        migrations.AddField(
            model_name='projectfacilitiesinfo',
            name='project_page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='facities', to='z_protofolio.projectpage'),
        ),
        migrations.AddField(
            model_name='projectgalleryimage',
            name='project_page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='z_protofolio.projectpage'),
        ),
    ]
