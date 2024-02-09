# Generated by Django 3.0.1 on 2024-02-09 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('number_of_likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Quran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField(default='Allah', max_length=100)),
                ('style', models.TextField(max_length=100)),
                ('language', models.TextField(default='arabic', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DhikrCard',
            fields=[
                ('feedcard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sajda_feed_app.FeedCard')),
                ('user_progress', models.IntegerField()),
                ('last_read_date', models.DateField()),
            ],
            bases=('sajda_feed_app.feedcard',),
        ),
        migrations.CreateModel(
            name='HadithCard',
            fields=[
                ('feedcard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sajda_feed_app.FeedCard')),
                ('hadith_book', models.TextField()),
                ('hadith_number', models.IntegerField()),
            ],
            bases=('sajda_feed_app.feedcard',),
        ),
        migrations.CreateModel(
            name='PictureCard',
            fields=[
                ('feedcard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sajda_feed_app.FeedCard')),
                ('image', models.ImageField(upload_to='inspiring_pictures/')),
            ],
            bases=('sajda_feed_app.feedcard',),
        ),
        migrations.CreateModel(
            name='QuranCard',
            fields=[
                ('feedcard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sajda_feed_app.FeedCard')),
                ('surah_number', models.IntegerField()),
                ('ayah_number', models.IntegerField()),
            ],
            bases=('sajda_feed_app.feedcard',),
        ),
        migrations.CreateModel(
            name='YouTubeCard',
            fields=[
                ('feedcard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sajda_feed_app.FeedCard')),
                ('preview_image', models.ImageField(upload_to='youtube_videos/')),
                ('in_app', models.BooleanField(default=False)),
            ],
            bases=('sajda_feed_app.feedcard',),
        ),
        migrations.CreateModel(
            name='Surah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.TextField()),
                ('mushaf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sajda_feed_app.Quran')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('default', 'Heart'), ('thumbs-up', 'Thumbs Up'), ('fire', 'Fire')], default='default', max_length=20)),
                ('feed_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sajda_feed_app.FeedCard')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hadith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('narrator', models.TextField(max_length=100)),
                ('hadith_text', models.TextField()),
                ('book', models.TextField(max_length=100)),
            ],
            options={
                'unique_together': {('number', 'book')},
            },
        ),
        migrations.CreateModel(
            name='Ayah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('text', models.TextField()),
                ('surah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sajda_feed_app.Surah')),
            ],
        ),
    ]
