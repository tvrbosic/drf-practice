from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user import models
from user.serializers import RegistrationSerializer

# Create your views here.


@api_view(['POST', ])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration successful!"
            data['username'] = account.username
            data['email'] = account.email
            # Along with next line we use post_save signal to create user token
            token = Token.objects.get(user=account).key
            # If using next line we do not need post_save signal hnadler for token generation
            # token = Token.objects.get_or_create(user=account).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data)
