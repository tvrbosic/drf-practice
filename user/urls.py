from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from user.views import logout_view, registration_view

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout_view, name='logout')
]
