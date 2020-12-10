from django.urls import path
from .views import *

app_name = 'quizy'

urlpatterns = [
    path('api/create-quiz/', api_create_quiz_view, name="create"),
    path('api/add-question/', api_add_mcq_view, name="add-mcq"),
    path('api/manage-quiz/', create_answer_view, name="manage"),
    path('api/attempt-quiz/', attempt_quiz, name="attempt_quiz"),
    
]
