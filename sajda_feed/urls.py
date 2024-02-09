from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from sajda_feed_app import views

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/feed_cards/', views.FeedCardList.as_view(), name="feed_cards")
]