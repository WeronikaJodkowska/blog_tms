from django.http import HttpResponse


def profiles(request):
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    return HttpResponse("Profiles index view")

# for key, value in request.POST.items():
#