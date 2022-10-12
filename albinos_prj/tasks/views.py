from django.shortcuts import render
from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(label="Название")
    priority = forms.IntegerField(
        label="Приоритет",
        min_value=0,
        max_value=10
    )


form = NewTaskForm()


def main(request):
    return render(
        request,
        "tasks/main.html"
    )


def index(request):
    return render(
        request,
        "tasks/index.html",
        {"tasks": ['Первое', 'Второе', 'Третье']}
    )


def form_page(request):
    return render(
        request,
        "tasks/form_page.html",
        {"form": form}
    )
