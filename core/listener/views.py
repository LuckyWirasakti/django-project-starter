from requests import post
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.listener.models import Listener
from django.conf import settings

# Create your views here.
class ListenerView(APIView):
    def post(self, request, format=None):
        listen  = Listener.objects.filter(active=True).values_list('url', flat=True)
        verify  = settings.VERIFY_SSL_REQUEST
        data    = request.data
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        success = 0
        failure = 0
        for url in listen:
            response = post(url=url, data=data, verify=verify, headers=headers)
            if response.status_code == 200:
                success += 1
            else :
                failure += 1
        data = {
            'success': success,
            'failure': failure
        }
        return Response(data=data, status=status.HTTP_200_OK)