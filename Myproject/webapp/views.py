from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializers, ReservationSerializer, CategorySerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ActivityAPIView(APIView):
	def get(self, request):
		activity = Activity.objects.filter()
		serializer = ActivitySerializers(activity, many=True)
		return Response(serializer.data)



class ReservationsAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReservationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		

class UserRegistrationView(generics.CreateAPIView):
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]

class UserLoginView(generics.GenericAPIView):
	serializer_class = UserSerializer

	def post(self, request):
		username = request.data.get('username')
		password = request.data.get('password')
		user = authenticate(username=username, password=password)
		if user:
			token, created = Token.objects.get_or_create(user=user)
			return Response({'token': token.key})
		return Response({'error': 'Identifiants invalides'}, status=400)
