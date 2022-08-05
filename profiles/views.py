import os
import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from profiles.forms import RegisterForm
from profiles.models import Address

logger = logging.getLogger(__name__)


def profiles(request):
    # Проверяем GET параметры и собираем сообщение
    message = []
    for key, value in request.GET.items():
        message.append(f"{key}={value}")

    # Проверяем POST параметры и выводим в консоль
    for key, value in request.POST.items():
        logger.info(f"POST param: {key}={value}")

    logger.info(f"Environment variable: {settings.ENV_VAR}")

    # 18_homework. В представлении вычитать настройки, и в зависимости от значения первой,
    # выводить в консоль значение второй или третьей.
    logger.info(f"MY_SETTING_1: {settings.MY_SETTING_1}")
    logger.info(f"MY_SETTING_1 = current directory? "
                f"{settings.MY_SETTING_2 if settings.MY_SETTING_1 == os.getcwd() else settings.MY_SETTING_3}")

    # Если были GET параметры в запросе, выводим соответствующее сообщение
    if len(message):
        return HttpResponse(f"Profile view with GET params: {', '.join(message)}")
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
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})