from django.contrib.auth.models import User


def create_user(
    email: str, username: str, first_name: str, last_name: str, password: str
):
    user = User(
        email=email, username=username, first_name=first_name, last_name=last_name
    )
    user.set_password(password)
    user.save()
