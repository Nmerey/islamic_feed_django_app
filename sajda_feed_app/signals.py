from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Like, FeedCard

@receiver(post_save, sender=Like)
@receiver(post_delete, sender=Like)
def update_feed_card_likes(sender, instance, **kwargs):
    # Update the number of likes for the associated FeedCard
    feed_card = instance.feed_card
    feed_card.number_of_likes = Like.objects.filter(feed_card=feed_card).count()
    feed_card.save()
