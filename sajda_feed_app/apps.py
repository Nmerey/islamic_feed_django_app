from django.apps import AppConfig


class SajdaFeedAppConfig(AppConfig):
    name = 'sajda_feed_app'

    def ready(self):
        from sajda_feed_app import signals
