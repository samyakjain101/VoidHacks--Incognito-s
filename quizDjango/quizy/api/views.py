from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from account.models import Account
from quizy.models import Quiz
from quizy.api.serializers import QuizSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'


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













# @api_view(['GET', ])
# def api_detail_blog_view(request, slug):

# 	try:
# 		quiz = BlogPost.objects.get(slug=slug)
# 	except BlogPost.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = QuizSerializer(quiz)
# 		return Response(serializer.data)


# @api_view(['PUT',])
# def api_update_blog_view(request, slug):

# 	try:
# 		quiz = BlogPost.objects.get(slug=slug)
# 	except BlogPost.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'PUT':
# 		serializer = QuizSerializer(quiz, data=request.data)
# 		data = {}
# 		if serializer.is_valid():
# 			serializer.save()
# 			data[SUCCESS] = UPDATE_SUCCESS
# 			return Response(data=data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE',])
# def api_delete_blog_view(request, slug):

# 	try:
# 		quiz = BlogPost.objects.get(slug=slug)
# 	except BlogPost.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'DELETE':
# 		operation = quiz.delete()
# 		data = {}
# 		if operation:
# 			data[SUCCESS] = DELETE_SUCCESS
# 		return Response(data=data)