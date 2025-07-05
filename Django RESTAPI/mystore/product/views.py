from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GoogleLoginView(APIView):
    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response({'error': 'Code is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        resp = requests.get(GOOGLE_USERINFO_URL, headers={"Authorization": f"Bearer {code}"})
        if resp.status_code != 200:
            return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        userinfo = resp.json()
        return Response(userinfo)