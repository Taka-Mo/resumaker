# Generated by Django 2.2.1 on 2019-05-07 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0005_auto_20190505_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumedata',
            name='temp',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
