# Generated by Django 3.2.8 on 2021-10-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка'),
        ),
    ]
