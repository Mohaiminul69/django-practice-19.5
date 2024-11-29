from django.urls import path
from .views import UserRegister, UserLoginView, ProfileView, UserLogoutView

urlpatterns = [
    path("sign_up", UserRegister.as_view(), name="register_page"),
    path("login/", UserLoginView.as_view(), name="login_page"),
    path("logout/", UserLogoutView.as_view(), name="logout_page"),
    path("profile/", ProfileView.as_view(), name="profile_page"),
]
