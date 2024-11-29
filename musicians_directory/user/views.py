from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Create your views here.
class UserRegister(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "sign_up.html"
    success_url = reverse_lazy("login_page")

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Register"
        return context


class UserLoginView(LoginView):
    template_name = "sign_up.html"

    def get_success_url(self):
        return reverse_lazy("homepage")

    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Login information is incorrect")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context


def user_logout(request):
    logout(request)
    return redirect("login_page")


@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
