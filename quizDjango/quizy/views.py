import uuid
import json
from datetime import timedelta, datetime #for timer 
from .models import *
from django.core.exceptions import PermissionDenied

# new import
from .forms import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# from account.models import Account
from .serializers import QuizSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# api views
@api_view(['POST'])
def api_create_quiz_view(request):

	# account = Account.objects.get(pk=1)
    quiz = Quiz()
	# quiz = Quiz(author=account)
    if request.method == 'POST':
        serializer = QuizSerializer(quiz, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# {
#     "quizid": "f989f553-fbb9-491d-8914-5593da601958",
#     "question": "This is que?",
#     "choice1": "Yes, i think",
#     "choice1bool": "True",
#     "choice2": "Yes, it is",
#     "choice2bool": "False",
#     "choice3": "No, i think",
#     "choice3bool": "False",
#     "choice4": "No, it is not",
#     "choice4bool": "False"
# }

@api_view(['POST'])
def api_add_mcq_view(request):

    data = JSONParser().parse(request)
    print(data)
    print(data["quizid"])

    try:
        quiz_id = uuid.UUID(data["quizid"]).hex
    except ValueError:
        raise PermissionDenied()

    try: 
        quiz = Quiz.objects.get(id = quiz_id)
        que = Question(quiz=quiz,question=data["question"])
        que.save()
        c1 = Choice(question=que,choice=data["choice1"],is_correct=data["choice1bool"])
        c1.save()
        c2 = Choice(question=que,choice=data["choice2"],is_correct=data["choice2bool"])
        c2.save()
        c3 = Choice(question=que,choice=data["choice3"],is_correct=data["choice3bool"])
        c3.save()
        c4 = Choice(question=que,choice=data["choice4"],is_correct=data["choice4bool"])
        c4.save()
        return Response(data, status=status.HTTP_201_CREATED)

    except Quiz.DoesNotExist:
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    