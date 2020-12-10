from django.urls import path
from .views import *

app_name = 'quizy'

urlpatterns = [
    path('api/create-quiz/', api_create_quiz_view, name="create"),
    path('api/add-question/', api_add_mcq_view, name="add-mcq"),
    path('api/manage-quiz/', create_answer_view, name="manage"),
    path('api/attempt-quiz/', AttempQuiz.as_view, name="attempt_quiz"),
    path('api/edit-quiz/', GetAllQue.as_view, name="edit_data"),

    #send all user
    path('api/send-users/', SendUsers.as_view(), name="send_users"),


]
