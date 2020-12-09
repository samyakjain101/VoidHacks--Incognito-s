from django.urls import path
from quizy.api.views import(
	# api_detail_blog_view,
	# api_update_blog_view,
	# api_delete_blog_view,
	api_create_quiz_view,
)

app_name = 'blog'

urlpatterns = [
	# path('<slug>/', api_detail_blog_view, name="detail"),
	# path('<slug>/update', api_update_blog_view, name="update"),
	# path('<slug>/delete', api_delete_blog_view, name="delete"),
	path('quiz/create', api_create_quiz_view, name="create"),
]