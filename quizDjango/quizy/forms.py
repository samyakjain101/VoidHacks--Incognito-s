from django import forms

from .models import Quiz


class CreateQuizForm(forms.ModelForm):

	class Meta:
		model = Quiz
		fields = ['start_date', 'end_date', 'title', 'duration']