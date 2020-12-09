from django.urls import path
from .views import *

#new
# from quizy.api.views import(
# 	api_create_quiz_view,
# )

app_name = 'quizy'

urlpatterns = [
    path('api/create-quiz/', api_create_quiz_view, name="create"),
    path('api/manage-quiz/', create_answer_view, name="manage"),
]
