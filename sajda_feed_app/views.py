from .models import FeedCard, Like, User, CustomUser
from .serializers import LikeSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import redirect


class FeedCardList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'feed_cards/index.html'

    def get(self, request):
        sub_classes = FeedCard.__subclasses__()
        queryset = {}

        access_token = request.GET.get('access_token')

        if access_token:
        	try:
        		current_user = User.objects.get(customuser__access_token=access_token)
        	except User.DoesNotExist:
        		current_user = None

        for sub_class in sub_classes:
        	subclass_name = sub_class.__name__

        	# Optimizing query by only extracting last 5 instances of each subcalss
        	# We can store number of last instances as env_var to better it
        	queryset[subclass_name] = sub_class.objects.order_by('-id')[:5]
        
        return Response({ 'card_list': queryset, 'current_user': current_user }, status=status.HTTP_200_OK)

class LikeCreateAPIView(APIView):
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(request.META.get('HTTP_REFERER'), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)