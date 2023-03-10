# Generated by Django 4.1.5 on 2023-01-18 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_posttag_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttag',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_tag', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
