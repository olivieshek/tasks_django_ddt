from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


class NewForm(forms.Form):
    dividend = forms.IntegerField(label="Делимое:")
    divider = forms.IntegerField(label="Делитель:")

    def whats_wrong_with_me(self, request):
        # принтим все проблемы
        form = NewForm(request.POST)
        for field in form:
            print("Field Error:", field.name, field.errors)

    def request_info(self, request):
        # принтим инфу про запрос
        print(request)
        print(request.POST)


history_list = list()


def index(request):
    return render(
        request,
        "real_app/index.html",
        {
            "title": "Real App"
        }
    )


def form_page(request):
    new_form = NewForm(request.POST)
    if request.method == "POST":
        new_form.whats_wrong_with_me(request)
        new_form.request_info(request)
        if new_form.is_valid():
            dividend = new_form.cleaned_data["dividend"]
            divider = new_form.cleaned_data["divider"]
            history_list.append(f'{dividend} + {divider} = {dividend + divider}')
            return HttpResponseRedirect(reverse("real_app:history"))
        else:
            return render(
                request,
                "real_app/not_valid.html",
                {
                    "title": "Error",
                    "form": new_form
                }
            )
    else:
        return render(
            request,
            "real_app/form_page.html",
            {"form": new_form}
        )


def history(request):
    return render(
        request,
        "real_app/history.html",
        {
            "title": "Operations History",
            "history_list": history_list
        }
    )