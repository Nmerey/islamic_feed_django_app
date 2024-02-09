from django.urls import path
from . import views

urlpatterns = [
    path('feed_cards/', views.FeedCardList.as_view(), name='feed-card-list'),
]