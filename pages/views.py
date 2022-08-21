from django.shortcuts import render

from django.views.generic import (
    TemplateView
)


class Register(TemplateView):
    template_name = 'register.html'
    page_name = "Register"

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)

        return context


class Login(TemplateView):
    template_name = 'login.html'
    page_name = "Login"

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)

        return context