from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager

# Authentification with access_token only
class CustomUser(models.Model):
	user 			= models.OneToOneField(User, on_delete=models.CASCADE)
	access_token 	= models.TextField(blank=False)

# Meta parent class for storing alike fields(title,description...)
class FeedCard(models.Model):
	title 			= models.CharField(max_length=100, blank=True)
	description 	= models.TextField(blank=True)
	number_of_likes = models.IntegerField(default=0)

	# Need this to hand child classes
	objects = InheritanceManager()

# Created separate class for likes to make it easier to do analytics
class Like(models.Model):
  LIKE_TYPES = (
      ('default', 'Heart'),
      ('thumbs-up', 'Thumbs Up'),
      ('fire', 'Fire'),
      # We can add more types if needed later
  )
  feed_card = models.ForeignKey(FeedCard, on_delete=models.CASCADE)
  owner 	= models.ForeignKey(User,on_delete=models.CASCADE)
  type 		= models.CharField(max_length=20, choices=LIKE_TYPES, default=LIKE_TYPES[0][0])

class QuranCard(FeedCard):
	arabic_text = models.TextField(max_length=100)
	ayah_number = models.IntegerField()

class HadithCard(FeedCard):
	narrator 	= models.TextField(max_length=100)
	hadith_text = models.TextField()

class PictureCard(FeedCard):
	image = models.ImageField(upload_to='inspiring_pictures/',default='https://placehold.co/600x400')

class DhikrCard(FeedCard):
	user_progress 	= models.IntegerField()
	last_read_date 	= models.DateField()

class YouTubeCard(FeedCard):
	video_id 		= models.TextField(max_length=100)
	preview_image 	= models.ImageField(upload_to='youtube_videos/',default='https://placehold.co/600x400')
	in_app 			= models.BooleanField(default=False)
