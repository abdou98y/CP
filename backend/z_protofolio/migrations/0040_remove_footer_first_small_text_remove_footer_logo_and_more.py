# Generated by Django 5.0.1 on 2024-08-30 15:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("z_protofolio", "0039_footer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="footer",
            name="first_small_text",
        ),
        migrations.RemoveField(
            model_name="footer",
            name="logo",
        ),
        migrations.RemoveField(
            model_name="footer",
            name="second_small_text",
        ),
        migrations.RemoveField(
            model_name="footer",
            name="theird_small_text",
        ),
    ]
