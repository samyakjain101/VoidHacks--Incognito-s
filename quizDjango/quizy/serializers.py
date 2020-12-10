from rest_framework import serializers

from .models import Quiz, QuizAnswerRecord


class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields = ['id' ,'start_date', 'end_date', 'title', 'duration',]

class QueRecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuizAnswerRecord
		fields = ['record','question','myAns','viewed']
