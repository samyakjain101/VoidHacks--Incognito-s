from django.urls import path
from .views import *

app_name = 'quizy'

urlpatterns = [
    path('api/create-quiz/', api_create_quiz_view, name="create"),
    path('api/add-mcq/', api_add_mcq_view, name="add-mcq"),
]
