# Generated by Django 4.1.5 on 2023-01-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
