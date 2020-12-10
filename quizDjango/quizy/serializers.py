from rest_framework import serializers

from .models import Quiz, QuizAnswerRecord, Question


class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields = ['start_date', 'end_date', 'title', 'duration',]

class QueRecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuizAnswerRecord
		fields = ['record','question','myAns','viewed']

class AllQuesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ['question']

