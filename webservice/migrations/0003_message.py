# Generated by Django 3.2.8 on 2021-10-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0002_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Subject')),
                ('body', models.TextField(verbose_name='Body')),
            ],
        ),
    ]
