from rest_framework import views, response, exceptions, permissions
from rest_framework.decorators import api_view
from . import serializer as user_serializer
from . import services
from . import authentication

# @api_view(['POST'])
class Register(views.APIView):

    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user=data)

        print(data)

        return response.Response(data=serializer.data)

# @api_view(['POST'])
class Login(views.APIView):

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = services.user_email_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Email or Password")
        
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Email or Password")


        token = services.create_token(user_id=user.id)

        resp = response.Response()

        resp.set_cookie(key="jwt", value=token, samesite='None', secure=True, httponly=True)

        return resp


class ViewUser(views.APIView):

    # Endpoint only used if authenticated

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)

class Logout(views.APIView):

    # Endpoint only used if authenticated

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie(key="jwt")
        resp.data = {"message": "Logged out successfully"}

        return resp

