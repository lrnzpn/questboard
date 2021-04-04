from django.shortcuts import render, redirect

from .forms import QuestboardForm
from .models import Questboard

# Create your views here.
def homepage(response):
    return render(response, "pages/homepage.html", {})

def all_questboards(response):
    qb = Questboard.objects.all()
    context = {
        'questboards': qb
    }
    return render(response, "pages/questboard/questboards.html", context)


def new_questboard(response):
    if response.method == 'POST': 
        form = QuestboardForm(response.POST)
        if form.is_valid():
            qb = Questboard()
            qb.name = form.cleaned_data['name']
            qb.description = form.cleaned_data['description']
            qb.required_stars = form.cleaned_data['required_stars']
            qb.save()
            return redirect('view_questboard', slug=qb.slug)
    else:
        form = QuestboardForm()
    
    context = {
        'form': form,
    }
    return render(response, "pages/questboard/new_questboard.html", context)


def view_questboard(response, slug):
    qb = Questboard.objects.get(slug=slug)
    
    if response.method == 'POST':
        qb.name = response.POST.get('name')
        qb.description = response.POST.get('description')
        qb.required_stars = response.POST.get('required_stars')
        qb.save()
        return redirect('view_questboard', slug=qb.slug)
    
    context = {
        'questboard': qb
    }
    return render(response, "pages/questboard/questboard.html", context)

def all_quests(response):
    # qb = Questboard.objects.all()
    # context = {
    #     'questboards': qb
    # }
    return render(response, "pages/questboard/questboards.html", context)


def new_quest(response):
    # if response.method == 'POST': 
    #     form = QuestboardForm(response.POST)
    #     if form.is_valid():
    #         qb = Questboard()
    #         qb.name = form.cleaned_data['name']
    #         qb.description = form.cleaned_data['description']
    #         qb.required_stars = form.cleaned_data['required_stars']
    #         qb.save()
    #         return redirect('view_questboard', slug=qb.slug)
    # else:
    #     form = QuestboardForm()
    
    # context = {
    #     'form': form,
    # }
    return render(response, "pages/questboard/new_questboard.html", context)


def view_quest(response, slug):
    # qb = Questboard.objects.get(slug=slug)
    
    # if response.method == 'POST':
    #     qb.name = response.POST.get('name')
    #     qb.description = response.POST.get('description')
    #     qb.required_stars = response.POST.get('required_stars')
    #     qb.save()
    #     return redirect('view_questboard', slug=qb.slug)
    
    # context = {
    #     'questboard': qb
    # }
    return render(response, "pages/questboard/questboard.html", context)