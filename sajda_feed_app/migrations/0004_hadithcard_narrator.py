# Generated by Django 3.0.1 on 2024-02-09 18:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sajda_feed_app', '0003_auto_20240209_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='hadithcard',
            name='narrator',
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
