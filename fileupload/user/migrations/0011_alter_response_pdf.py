# Generated by Django 3.2.2 on 2021-08-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_response_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='pdf',
            field=models.FileField(upload_to='media'),
        ),
    ]