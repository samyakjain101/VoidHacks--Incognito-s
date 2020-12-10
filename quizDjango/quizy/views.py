import uuid
import json
import random
from datetime import timedelta, datetime #for timer 
from .models import *
from django.core.exceptions import PermissionDenied

# new import
from .forms import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from knox.auth import TokenAuthentication


# from account.models import Account
from .serializers import QuizSerializer,QueRecordSerializer,AllQuesSerializer
from django.core import serializers

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

@api_view(['POST'])
def api_add_mcq_view(request):

    data = JSONParser().parse(request)
    print(data)
    print(data["quiz_id"])

    try:
        quiz_id = uuid.UUID(data["quiz_id"]).hex
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

    
@api_view(['GET'])
def create_answer_view(request):
    if request.method == 'GET':
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

class IsLoggedInView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        Quuid = request.GET.get("quiz_id")

        try:
            quiz_id = uuid.UUID(Quuid).hex
        except ValueError:
            return Response("id value error", status=status.HTTP_400_BAD_REQUEST)

        try: 
            quiz = Quiz.objects.get(id = quiz_id)
        except Quiz.DoesNotExist:
            return Response("Quiz id don't exist", status=status.HTTP_400_BAD_REQUEST)

        ques = Question.objects.all()
        serializer = AllQuesSerializer(ques, many=True)
        return Response(serializer.data)    

class AttempQuiz(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        data = request.GET.get("quiz_id")
        print(data)

        try:
            quiz_id = uuid.UUID(data).hex
        except ValueError:
            return Response("id value error", status=status.HTTP_400_BAD_REQUEST)

        try: 
            quiz = Quiz.objects.get(id = quiz_id)
        except Quiz.DoesNotExist:
            return Response("Quiz id don't exist", status=status.HTTP_400_BAD_REQUEST)

        #Check if user is attempting quiz first time.
        #If not Permission Denied.
        if quiz.start_date <= timezone.now() and quiz.end_date > timezone.now():
            # print("myuser: "+ str(request.user) )
            # obj, created = QuizRecord.objects.get_or_create(user=request.user, quiz=quiz)
            obj, created = QuizRecord.objects.get_or_create(user=request.user, quiz=quiz)
            if created:
                qlist = random.shuffle(quiz.question_set.all())
                QuizAnswerRecord.objects.bulk_create(
                    [QuizAnswerRecord(record = obj, question = x) for x in qlist]
                )
            else:
                if obj.start + quiz.duration < timezone.now() or obj.is_submitted:
                    return Response("time over 1", status=status.HTTP_400_BAD_REQUEST)
            
            #here sending que 1 by 1
            try:
                quiz_record = QuizRecord.objects.get(user=request.user, quiz=quiz)
                currQue = quiz_record.quizanswerrecord_set.all().filter(viewed=False)[0].question

                quiz_record.viewed = True
                quiz_record.save()

                unViewed = list( Choice.objects.all().filter(question=currQue) )
                unViewed.append(currQue)
                json_unViewed = serializers.serialize('json', unViewed, use_natural_keys=True)

                serializer = QueRecordSerializer(currQue)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response("{}", status=status.HTTP_201_CREATED)
        else:
            return Response("time over final", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        #quiz_id
        #question_id
        #answer choice id
        data = JSONParser().parse(request)
        print(data)
        print(data["quiz_id"])

        try:
            quiz_id = uuid.UUID(data["quiz_id"]).hex
        except ValueError:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        try: 
            quiz = Quiz.objects.get(id = quiz_id)
            try:
                que = Question.objects.get(id=data["ques_id"])
                mychoice = Choice.objects.get(id=data["choice_id"])
                myRec = QuizRecord.objects.get(user=request.user,quiz=quiz)
                myQRec = QuizAnswerRecord.objects.get(record=myRec,question=que)

                myQRec.myAns = mychoice
                myQRec.viewed = True
                myQRec.save()
                return Response(data, status=status.HTTP_201_CREATED)

            except Question.DoesNotExist:
                return Response("Question dont exist", status=status.HTTP_400_BAD_REQUEST)

        except Quiz.DoesNotExist:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)