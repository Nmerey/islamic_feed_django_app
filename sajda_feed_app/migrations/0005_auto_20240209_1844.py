# Generated by Django 3.0.1 on 2024-02-09 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sajda_feed_app', '0004_hadithcard_narrator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ayah',
            name='surah',
        ),
        migrations.DeleteModel(
            name='Hadith',
        ),
        migrations.RemoveField(
            model_name='surah',
            name='mushaf',
        ),
        migrations.DeleteModel(
            name='Ayah',
        ),
        migrations.DeleteModel(
            name='Quran',
        ),
        migrations.DeleteModel(
            name='Surah',
        ),
    ]
