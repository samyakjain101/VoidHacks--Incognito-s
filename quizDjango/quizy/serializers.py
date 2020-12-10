from rest_framework import serializers

from .models import Quiz, QuizAnswerRecord, Question
from django.contrib.auth.models import User

class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields = ['id' ,'start_date', 'end_date', 'title', 'duration',]

class QueRecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuizAnswerRecord
		fields = ['record','question','myAns','viewed']

class AllQuesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ['question']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','first_name','last_name','email','username']
