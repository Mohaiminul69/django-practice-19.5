from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "User Registered Succesfully")
            return redirect("login_page")
    else:
        register_form = RegistrationForm()
    return render(request, "sign_up.html", {"form": register_form, "type": "Register"})


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


@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile_page")
    else:
        profile_form = ChangeUserForm(instance=request.user)
    return render(request, "update_profile.html", {"form": profile_form})
