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
from rest_framework.authtoken.models import Token

# from account.models import Account
from .serializers import QuizSerializer,QueRecordSerializer,AllQuesSerializer,UserSerializer
from django.core import serializers

#mail
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings # for getting from mail (sending mail)


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

        ans = data["choice"]        

        c1 = Choice(question=que,choice=data["choice1"],is_correct=True if (ans=="1") else False)
        c1.save()
        c2 = Choice(question=que,choice=data["choice2"],is_correct=True if (ans=="2") else False)
        c2.save()
        c3 = Choice(question=que,choice=data["choice3"],is_correct=True if (ans=="3") else False)
        c3.save()
        c4 = Choice(question=que,choice=data["choice4"],is_correct=True if (ans=="4") else False)
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

class GetAllQue(APIView):
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

    def post(self, request, format=None):
        #quiz_id
        #question_id
        #answer choice id
        #todo
        data = JSONParser().parse(request)
        print(data)
        # print(data["quiz_id"])
        todo = data["todo"]

        if(todo == True):

            try:
                quiz_id = uuid.UUID(data["quiz_id"]).hex
            except ValueError:
                return Response("id value error", status=status.HTTP_400_BAD_REQUEST)

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
                    # return Response(data, status=status.HTTP_201_CREATED)

                    #From here, procedure of showingnext question

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
                            
                            #below 1st line will give remaining time in seconds
                            timeLeftInSec = startTimer(quiz.end_date,quiz_record.start,quiz.duration)
                            if(timeLeftInSec == None):
                                return Response("time over acc. to startTimer func()", status=status.HTTP_400_BAD_REQUEST)        

                            currQue = quiz_record.quizanswerrecord_set.all().filter(viewed=False)[0].question

                            quiz_record.viewed = True
                            quiz_record.save()

                            choices = Choice.objects.all().filter(question=currQue)
                            # unViewed.append(currQue)
                            # unViewed.append(timeLeftInSec)
                            ans = [
                                    {
                                        "timeLeftInSec" : timeLeftInSec,
                                    },
                                    {
                                        "question" : currQue.question,
                                        "ques_id" : currQue.id
                                    },
                                    {
                                        "id": choices[0].id,
                                        "choice": choices[0].choice,
                                        "is_correct": choices[0].is_correct
                                    },
                                    {
                                        "id": choices[1].id,
                                        "choice": choices[1].choice,
                                        "is_correct": choices[1].is_correct
                                    },
                                    {
                                        "id": choices[2].id,
                                        "choice": choices[2].choice,
                                        "is_correct": choices[2].is_correct
                                    },
                                    {
                                        "id": choices[3].id,
                                        "choice": choices[3].choice,
                                        "is_correct": choices[3].is_correct
                                    },
                                ]
                            return Response(ans, status=status.HTTP_201_CREATED)
                        except:
                            return Response("{}", status=status.HTTP_201_CREATED)
                    else:
                        return Response("time over final", status=status.HTTP_400_BAD_REQUEST)

                except Question.DoesNotExist:
                    return Response("Question dont exist", status=status.HTTP_400_BAD_REQUEST)

            except Quiz.DoesNotExist:
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
        elif(todo == False):
            try:
                quiz_id = uuid.UUID(data["quiz_id"]).hex
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
                    qlist = quiz.question_set.all()
                    QuizAnswerRecord.objects.bulk_create(
                        [QuizAnswerRecord(record = obj, question = x) for x in qlist]
                    )
                
                else:
                    if obj.start + quiz.duration < timezone.now() or obj.is_submitted:
                        return Response("time over 1", status=status.HTTP_400_BAD_REQUEST)
                
                #here sending que 1 by 1
                try:
                    quiz_record = QuizRecord.objects.get(user=request.user, quiz=quiz)
                    print(quiz_record.quizanswerrecord_set.all())
                    currQue = quiz_record.quizanswerrecord_set.all().filter(viewed=False)[0].question

                    #below 1st line will give remaining time in seconds
                    timeLeftInSec = startTimer(quiz.end_date,quiz_record.start,quiz.duration)
                    
                    if(timeLeftInSec == None):
                        return Response("time over acc. to startTimer func()", status=status.HTTP_400_BAD_REQUEST)        

                    quiz_record.viewed = True
                    quiz_record.save()

                    unViewed = list( Choice.objects.all().filter(question=currQue) )
                    # unViewed.append(currQue)
                    # json_unViewed = serializers.serialize('json', unViewed, use_natural_foreign_keys=True, use_natural_primary_keys=True)
                    choices = Choice.objects.all().filter(question=currQue)
                            
                    ans = [
                            {
                                "timeLeftInSec" : timeLeftInSec,
                            },
                            {
                                "question" : currQue.question,
                                "ques_id" : currQue.id
                            },
                            {
                                "id": choices[0].id,
                                "choice": choices[0].choice,
                                "is_correct": choices[0].is_correct
                            },
                            {
                                "id": choices[1].id,
                                "choice": choices[1].choice,
                                "is_correct": choices[1].is_correct
                            },
                            {
                                "id": choices[2].id,
                                "choice": choices[2].choice,
                                "is_correct": choices[2].is_correct
                            },
                            {
                                "id": choices[3].id,
                                "choice": choices[3].choice,
                                "is_correct": choices[3].is_correct
                            },
                        ]

                    # serializer = QueRecordSerializer(currQue)
                    return Response(ans, status=status.HTTP_201_CREATED)
                except:
                    
                    return Response("{}", status=status.HTTP_201_CREATED)
            else:
                return Response("time over final", status=status.HTTP_400_BAD_REQUEST)



def send_email(subject,message,from_email,to_mail):
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, to_mail, fail_silently=True)
        except BadHeaderError:
            send_mail("Invalid header found in sent below email", "Subject : " + subject + "\n" + "Message : " + message, from_email, from_email, fail_silently=True)
            #return HttpResponse('Invalid header found.')
        #return HttpResponseRedirect('/contact/thanks/')
    else:
        send_mail("all field not filled error in sent below email", "Subject : " + subject + "\n" + "Message : " + message, from_email, from_email, fail_silently=True)


class SendUsers(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        usr = User.objects.all()
        serializer = UserSerializer(usr, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):

        try:
            data = JSONParser().parse(request)
            print(data)
            print(data["listOfIds"])

            lst = data["listOfIds"]
            try:
                quiz_id = uuid.UUID(data["quiz_id"]).hex
            except ValueError:
                return Response("id value error", status=status.HTTP_400_BAD_REQUEST)

            try: 
                quiz = Quiz.objects.get(id = quiz_id)
            except Quiz.DoesNotExist:
                return Response("Quiz id don't exist", status=status.HTTP_400_BAD_REQUEST)

            
            for usr in lst:
                token = Token.objects.get_or_create(user=User.objects.get(id=usr))
                # print(token.key)
            
            print(data["listOfIds"])
            for usr in lst:
                message = '{} invited you to give {} Quiz on Quizy. Go to http://192.168.225.24:4200/{}/{}/ to start.'.format(
                    request.user.username,
                    quiz.title,
                    Token.objects.get(user=User.objects.get(id=usr)).key,
                    quiz.id
                )
                subject = "You have 1 Quizy Invitation!"
                from_email = settings.EMAIL_HOST_USER
                to_mail = [User.objects.get(id=usr).email]
                #Send email to selected user
                send_email(subject,message,from_email,to_mail)

            # print(data["listOfIds"])

            return Response("send mail to all", status=status.HTTP_201_CREATED)
        except:
            return Response("Some error occured", status=status.HTTP_400_BAD_REQUEST)




def startTimer(quizEndDate,recordStartDate,quizDuration):
    #below for timer
    #For setting time for js timer:
    # (end date - start date) = Total duration or Td
    Td = quizEndDate - recordStartDate
    if Td > quizDuration:  # case 1: Td > d -> timerDuration = d
        timerDuration = quizDuration
    elif Td < quizDuration: # case 2: Td < d -> timerDuration = Td
        timerDuration = Td 
    elif Td == quizDuration: # case 3: Td == d -> timerDuration = d
        timerDuration = quizDuration
    
    recordEndDate = recordStartDate + timerDuration
    
    if recordEndDate < datetime.now(tz=recordEndDate.tzinfo):
        return None

    return int(timerDuration.total_seconds())