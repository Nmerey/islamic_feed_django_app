from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(FeedCard)
admin.site.register(QuranCard)
admin.site.register(HadithCard)
admin.site.register(PictureCard)
admin.site.register(YouTubeCard)
admin.site.register(Like)