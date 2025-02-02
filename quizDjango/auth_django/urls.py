from .views import RegisterAPI
from django.urls import path


from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/isloggedin/', IsLoggedInView.as_view(), name='isloggedin'),
]