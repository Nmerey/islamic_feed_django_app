from django.db import models
from django.contrib.auth.models import User

# Meta parent class for storing alike fields(title,description...)
class FeedCard(models.Model):
	title = models.CharField(max_length=100, blank=True)
	description = models.TextField(blank=True)
	number_of_likes = models.IntegerField(default=0)

# Created separate class for likes to make it easier to do analytics
class Likes(models.Model):
  LIKE_TYPES = (
      ('default', 'Heart'),
      ('thumbs-up', 'Thumbs Up'),
      ('fire', 'Fire'),
      # We can add more types if needed later
  )
  feed_card = models.ForeignKey(FeedCard, on_delete=models.CASCADE)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)
  type = models.CharField(max_length=20, choices=LIKE_TYPES, default=LIKE_TYPES[0][0])

class QuranCard(FeedCard):
	surah_number = models.IntegerField()
	ayah_number = models.IntegerField()

class HadithCard(FeedCard):
	hadith_book = models.TextField(max_length=100)
	hadith_number = models.IntegerField()

# Separate Quran class for translations too
class Quran(models.Model):
	author = models.TextField(max_length=100, default='Allah')
	style = models.TextField(max_length=100)
	language = models.TextField(max_length=100, default='arabic')

class Surah(models.Model):
	number = models.IntegerField()
	name = models.TextField()
	mushaf = models.ForeignKey(Quran, on_delete=models.CASCADE)

class Ayah(models.Model):
	number = models.IntegerField()
	text = models.TextField()
	surah = models.ForeignKey(Surah, on_delete=models.CASCADE)

class Hadith(models.Model):
	number = models.IntegerField()
	narrator = models.TextField(max_length=100)
	hadith_text = models.TextField()
	book = models.TextField(max_length=100)

	class Meta:
		unique_together = ('number', 'book')

class PictureCard(FeedCard):
	image = models.ImageField(upload_to='inspiring_pictures/')

class DhikrCard(FeedCard):
	user_progress = models.IntegerField()
	last_read_date = models.DateField()

class YouTubeCard(FeedCard):
	preview_image = models.ImageField(upload_to='youtube_videos/')
	in_app = models.BooleanField(default=False)
