from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from sajda_feed_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/feed_cards/', views.FeedCardList.as_view(), name="feed_cards"),
    path('api/likes/', views.LikeCreateAPIView.as_view(), name='like_create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()