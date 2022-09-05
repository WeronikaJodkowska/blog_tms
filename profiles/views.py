import os
import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

from profiles.forms import RegisterForm, LoginForm
from profiles.models import Address
from profiles.services import create_user

logger = logging.getLogger(__name__)


def profiles(request):
    return HttpResponse("Profile view")


# 19_homework. 2. Добавить во вьюшку поиск по GET параметру используя соответствующее поле в модели.
def get_address(request):
    city = request.GET.get("city")
    if city:
        address_list = Address.objects.filter(city__contains=city)
    else:
        address_list = Address.objects.all()
    return HttpResponse(", ".join([x.user.username for x in address_list]) + f" live in {city}")


def register(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            create_user(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                password=form.cleaned_data["password"],
            )
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")
