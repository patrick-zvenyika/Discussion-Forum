# Generated by Django 3.2.2 on 2021-08-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_response_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
