from .models import FeedCard
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class FeedCardList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'feed_cards/index.html'

    def get(self, request):
        queryset = FeedCard.objects.all()
        return Response({'feed_cards': queryset})