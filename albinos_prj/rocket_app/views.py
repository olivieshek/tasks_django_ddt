from django.shortcuts import render


def index(request):
    return render(
        request,
        "rocket_app/index.html",
        {
            "title": "Homepage",
            "username": "Vitally"
        }
    )


def is_newyear(request):
    return render(
        request,
        "is_newyear/index.html"
    )
