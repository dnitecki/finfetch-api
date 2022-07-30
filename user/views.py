from rest_framework import views, response, exceptions, permissions
from . import serializer as user_serializer
from . import services

class Register(views.APIView):

    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user=data)

        print(data)

        return response.Response(data=serializer.data)


class Login(views.APIView):

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

