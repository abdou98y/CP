# Generated by Django 5.1 on 2024-08-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_protofolio', '0037_projectpage_contact_us_button_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuspage',
            name='contactus_button_title',
            field=models.CharField(default='contact us', max_length=100),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='download_button_title',
            field=models.CharField(default='download', max_length=100),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='show_founders',
            field=models.BooleanField(default=False),
        ),
    ]
