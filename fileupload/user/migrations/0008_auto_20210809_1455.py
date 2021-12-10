# Generated by Django 3.2.2 on 2021-08-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210805_0629'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
        migrations.AddField(
            model_name='response',
            name='filepath',
            field=models.FileField(default='', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(null=True),
        ),
    ]