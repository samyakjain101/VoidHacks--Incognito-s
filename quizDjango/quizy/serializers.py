from rest_framework import serializers

from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields = ['start_date', 'end_date', 'title', 'duration',]