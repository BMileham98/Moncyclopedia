from django.shortcuts import render, get_object_or_404 #throw an error for user if request isn't valid
from django.http import HttpResponse
from .models import Monster, Observation, Comment
from datetime import date

# Create your views here.

#home page function to allow featured monster
def index(request):
    monsters= Monster.objects.all()
    if monsters:
        today= date.today()
        #determining featured monster by element per weekday
        element_schedule = {
            0: 'Chaos',
            1: 'Holy',
            2: 'Marine',
            3: 'Nature',
            4: 'Aeries',
            5: 'Pyro',
            6: 'Twilight',
        }
        weekday = today.weekday()
        today_element= element_schedule[weekday]
        #sort monsters by element/category
        element_monsters = monsters.filter(category=today_element)
        if element_monsters:
            monster_index= today.toordinal() % element_monsters.count()
            featured_monster = element_monsters[monster_index]
            featured_element= today_element
        else: #if no monsters of this element, cycle through monsters
            monster_index= today.toordinal() % monsters.count()
            featured_monster = monsters[monster_index]
            featured_element= None
    else: #if no monsters are recalled, both are set to None
        featured_monster = None
        featured_element= None
    return render(request, 'index.html', {
        'featured_monster': featured_monster,
        'featured_element': featured_element,
    })


# view for masterlist of monsters catalogued
def monster_list(request):
    monsters = Monster.objects.all()
    return render(request, 'monster_list.html', {'monsters': monsters})

#view for each individual monster with list of related observations
def monster_detail(request, pk):
    monster = get_object_or_404(Monster, pk=pk)
    observations = monster.observations.all()
    return render(request, 'monster_detail.html', {'monster': monster, 'observations': observations})

#view for masterlist of observations by users
def observation_list(request):
    observations = Observation.objects.all()
    return render(request, 'observation_list.html', {'observations': observations})

#view for each individual observation
def observation_detail(request, slug):
    observation = get_object_or_404(Observation, slug=slug)
    return render(request, 'observation_detail.html', {'observation': observation})