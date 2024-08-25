# Generated by Django 5.1 on 2024-08-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_text', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('big_text', models.TextField()),
                ('image', models.ImageField(upload_to='z_protofolio/media')),
            ],
        ),
    ]
