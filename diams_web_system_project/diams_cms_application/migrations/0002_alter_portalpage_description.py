# Generated by Django 5.0.6 on 2024-05-31 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diams_cms_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portalpage',
            name='description',
            field=models.TextField(),
        ),
    ]
