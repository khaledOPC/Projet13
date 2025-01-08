from rest_framework import serializers
from .models import Category, Activity
from django.contrib.auth import get_user_model


User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ["name", "description"]


class ActivitySerializer(serializers.ModelSerializer):
	category = CategorySerializer()
	class Meta:
		model = Activity
		fields = ["name", "lieu", "date", "category"]


class ReservationSerializer(serializers.ModelSerializer):
	activity = ActivitySerializers()
	class Meta:	
		model = Reservation
		fields = ["date", "user", "activity"]


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user