# Generated by Django 3.2.2 on 2021-08-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_response_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='pdf',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]
