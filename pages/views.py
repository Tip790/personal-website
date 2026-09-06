from django.shortcuts import render

tasks = [
    {"title": "Finish Homework 1", "completed": False},
    {"title": "Graduate College", "completed": False},
    {"title": "Finish Quiz 2", "completed": False},
    {"title": "Sleep", "completed": True},
    {"title": "Play Video Games", "completed": True},
]


def home(request):
    return render(request, "home.html", {"tasks": tasks})
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")