from django.test import TestCase
from django.db.models.signals import post_save, post_delete
from django.dispatch import Signal
from .signals import update_feed_card_likes
from .models import *
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

class SignalTests(TestCase):
    def test_update_feed_card_likes_on_delete(self):
        feed_card = FeedCard.objects.create()
        user 			= User.objects.create(username='test_user')
        like 			= Like.objects.create(feed_card=feed_card, owner=user)

        # Check if the number of likes is updated after creating the Like object
        self.assertEqual(feed_card.number_of_likes, 1)

        like.delete()

        # Check if the number of likes is updated after deleting the Like object
        self.assertEqual(feed_card.number_of_likes, 0)

class DhikrCardTestCase(TestCase):
    def test_valid_user_progress(self):
        # Test valid user_progress (within range)
        dhikr_card = DhikrCard.objects.create(title='Dhikr Title', description='Dhikr Description', user_progress=50, last_read_date='2022-01-01')
        self.assertIsInstance(dhikr_card, DhikrCard)

    def test_invalid_user_progress_lower_bound(self):
        # Test invalid user_progress (below lower bound)
        with self.assertRaises(IntegrityError):
            DhikrCard.objects.create(title='Dhikr Title', description='Dhikr Description', user_progress=-1, last_read_date='2022-01-01')

    def test_invalid_user_progress_upper_bound(self):
        # Test invalid user_progress (above upper bound)
        with self.assertRaises(IntegrityError):
            DhikrCard.objects.create(title='Dhikr Title', description='Dhikr Description', user_progress=101, last_read_date='2022-01-01')

class ModelsTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_custom_user_creation(self):
        # Test CustomUser creation
        custom_user = CustomUser.objects.create(user=self.user, access_token='test_token')
        self.assertIsInstance(custom_user, CustomUser)

    def test_feed_card_creation(self):
        # Test FeedCard creation
        feed_card = FeedCard.objects.create(title='Test Title', description='Test Description')
        self.assertIsInstance(feed_card, FeedCard)

    def test_like_creation(self):
        # Test Like creation
        like = Like.objects.create(feed_card=FeedCard.objects.create(), owner=self.user, type='default')
        self.assertIsInstance(like, Like)

    def test_quran_card_creation(self):
        # Test QuranCard creation
        quran_card = QuranCard.objects.create(title='Quran Title', description='Quran Description', arabic_text='Arabic Text', ayah_number=1)
        self.assertIsInstance(quran_card, QuranCard)

    def test_hadith_card_creation(self):
        # Test HadithCard creation
        hadith_card = HadithCard.objects.create(title='Hadith Title', description='Hadith Description', narrator='Narrator', hadith_text='Hadith Text')
        self.assertIsInstance(hadith_card, HadithCard)

    def test_picture_card_creation(self):
        # Test PictureCard creation
        picture_card = PictureCard.objects.create(title='Picture Title', description='Picture Description', image='path/to/image.jpg')
        self.assertIsInstance(picture_card, PictureCard)

    def test_dhikr_card_creation(self):
        # Test DhikrCard creation
        dhikr_card = DhikrCard.objects.create(title='Dhikr Title', description='Dhikr Description', user_progress=50, last_read_date='2022-01-01')
        self.assertIsInstance(dhikr_card, DhikrCard)

    def test_youtube_card_creation(self):
        # Test YouTubeCard creation
        youtube_card = YouTubeCard.objects.create(title='YouTube Title', description='YouTube Description', video_id='123456')
        self.assertIsInstance(youtube_card, YouTubeCard)
