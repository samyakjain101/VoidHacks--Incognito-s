from django.urls import path
from .views import *

#new
# from quizy.api.views import(
# 	# api_detail_blog_view,
# 	# api_update_blog_view,
# 	# api_delete_blog_view,
# 	api_create_quiz_view,
# )

app_name = 'quiz_app'

urlpatterns = [
    #new
    path('quiz/create-quiz', create_quiz, name="create_quiz"),
    
    #api
    # path('quiz/create', api_create_quiz_view, name="create"),

    # past
    path('quiz/available', AvailableQuiz.as_view(), name="available_quiz"),
    path('quiz/check/<quiz_id>', attempt_quiz, name="attempt_quiz"),
    path('quiz/result/<quiz_id>', QuizResult.as_view(), name="quiz_result"),
    # path('ajax/live/quiz',save_answer, name="ajax_save_live_quiz"),
    path('live/quiz/<quiz_id>',liveQuiz, name="live_quiz_new"),
    path('live/quiz/end/<quiz_id>',end_quiz, name="end_quiz"),
    path('quiz/results',Results.as_view(), name="results"),
]
