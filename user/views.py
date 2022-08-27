from rest_framework import views, response, exceptions, permissions
from django.http import JsonResponse
from django.middleware.csrf import get_token
from . import serializer as user_serializer
from . import services
from . import authentication
from django.views.decorators.csrf import csrf_exempt

def get_csrf(request):
    response = JsonResponse({"Info": "Success - Set CSRF cookie"})
    response["X-CSRFToken"] = get_token(request)
    return response

class Register(views.APIView):
    @csrf_exempt
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user=data)

        return response.Response(data=serializer.data)

class Login(views.APIView):
    @csrf_exempt
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

        resp.set_cookie(key="jwt", value=token, httponly=True, secure=True,samesite="None", path="/")
        # resp.set_cookie(key="jwt", value=token, httponly=True) #FOR POSTMAN
        return resp


class ViewUser(views.APIView):
    

    # Endpoint only used if authenticated

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)

class Logout(views.APIView):

    # Endpoint only used if authenticated

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def post(self, request):
        resp = response.Response()
        resp.delete_cookie(key="jwt",samesite="None")
        # resp.delete_cookie(key="jwt",samesite="None") #POSTMAN
        resp.data = {"message": "Logged out successfully"}

        return resp

