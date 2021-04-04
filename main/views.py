from django.shortcuts import render

# Create your views here.
def homepage(response):
    context = {}
    return render(response, "pages/homepage.html", context)