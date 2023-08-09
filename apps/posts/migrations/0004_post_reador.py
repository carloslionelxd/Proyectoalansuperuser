# Generated by Django 4.2.3 on 2023-07-31 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reador',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posteos_usario', to=settings.AUTH_USER_MODEL),
        ),
    ]