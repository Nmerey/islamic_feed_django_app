from django.test import TestCase
from django.db.models.signals import post_save, post_delete
from django.dispatch import Signal
from .signals import update_feed_card_likes

from .models import FeedCard, Like
from django.contrib.auth.models import User

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