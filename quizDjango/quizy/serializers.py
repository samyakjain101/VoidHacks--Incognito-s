<<<<<<< HEAD
from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
=======
# from rest_framework import serializers

# from quizy.models import Quiz


# class QuizSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Quiz
# 		fields = ['start_date', 'end_date', 'title', 'duration']
>>>>>>> 5f9caa15e297fff245dba61f1b3b1f3f72a8707e
