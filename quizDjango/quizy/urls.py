from django.urls import path
from .views import *

#new
from quizy.api.views import(
	api_create_quiz_view,
)

app_name = 'quizy'

urlpatterns = [
    path('quiz/create', api_create_quiz_view, name="create"),
]
