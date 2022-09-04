from django.urls import path
from user import views

app_name = 'user'

urlpatterns= [
    path("register/", views.Register.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path("user/", views.ViewUser.as_view(), name="user"),
    path("logout/", views.Logout.as_view(), name="logout")
]