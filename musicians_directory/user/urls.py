from django.urls import path
from .views import UserRegister, UserLoginView, user_logout, ProfileView

urlpatterns = [
    path("sign_up", UserRegister.as_view(), name="register_page"),
    path("login/", UserLoginView.as_view(), name="login_page"),
    path("logout", user_logout, name="logout_page"),
    path("profile/", ProfileView.as_view(), name="profile_page"),
]
