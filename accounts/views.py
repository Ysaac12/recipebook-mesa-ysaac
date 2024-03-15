from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

class CustomView(LoginRequiredMixin, TemplateView):
    template_name = "registration/login.html"
    redirect_field_name="accounts/login"