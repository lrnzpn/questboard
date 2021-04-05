from django.shortcuts import render, redirect

from .forms import QuestboardForm, QuestForm
from .models import Questboard, Quest

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
        quest_form = QuestForm(response.POST)
        if response.POST.get('update'):
            qb.name = response.POST.get('qbName')
            qb.description = response.POST.get('qbDescription')
            qb.required_stars = response.POST.get('required_stars')
            qb.save()
            return redirect('view_questboard', slug=qb.slug)
        elif quest_form.is_valid() and response.POST.get('addQuest'):
            quest = Quest()
            quest.questboard = qb
            quest.name = quest_form.cleaned_data['name']
            quest.description = quest_form.cleaned_data['description']
            quest.stars = response.POST.get('stars')
            quest.is_for_everyone = quest_form.cleaned_data['is_for_everyone']
            quest.slots = response.POST.get('slots')
            quest.save()
            return redirect('view_questboard', slug=qb.slug)
        
    else:
        quest_form = QuestForm()
        
    quests = Quest.objects.filter(questboard_id=qb.id)
    
    context = {
        'questboard': qb,
        'quest_form':quest_form,
        'quests': quests
    }
    return render(response, "pages/questboard/questboard.html", context)


