from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
import random as r

from . import util


class NewForm(forms.Form):
    title = forms.CharField(label="Title ")
    body = forms.CharField(label="Details ", widget=forms.Textarea())


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def random(request):
    l = util.list_entries()
    l = l[r.randrange(len(l)-1)]
    return HttpResponseRedirect(reverse("content", kwargs={'title': l, 'view': 1}))


def content(request, title, view):
    body = util.get_entry(title)
    if view:
        return render(request, "encyclopedia/content.html", {
            "value": markdown2.markdown(body),
            "title": title,
        })
    return render(request, "encyclopedia/edit.html", {
        "update": 1,
        "form": NewForm(initial={'title': title, 'body': body}),
    })


def newPage(request):
    return render(request, "encyclopedia/edit.html", {
        "update": 0,
        "form": NewForm(),
    })


def add(request, update):
    title = ""
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data["body"]
            title = form.cleaned_data["title"]
            if update != 1 and title in util.list_entries():
                return render(request, "encyclopedia/error.html")
            util.save_entry(title, body)
    return HttpResponseRedirect(reverse("content", kwargs={'title': title, 'view': 1}))


def search(request):
    value = (request.POST).get("value")
    l = util.list_entries()
    if value in l:
        return HttpResponseRedirect(
            reverse("content", kwargs={'title': value, 'view': 1}))
    return render(request, "encyclopedia/index.html", {
        "entries": [i for i in l if value.lower() in i.lower()]
    })
