from django.shortcuts import render, get_object_or_404, redirect #throw an error for user if request isn't valid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Monster, Observation, Comment
from .forms import CommentForm
from datetime import date

# Create your views here.

#home page function to allow featured monster
def index(request):
    monsters= Monster.objects.all()
    if monsters:
        today= date.today()
        #determining featured monster by element per weekday
        weekday_names = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday',
        }
        
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
        today_weekday= weekday_names[weekday]
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
        'day_name': today_weekday,
    })


# view for masterlist of monsters catalogued
def monster_list(request):
    monsters = Monster.objects.all().order_by('name')
    return render(request, 'articles/monster_list.html', {'monsters': monsters})

#view for each individual monster with list of related observations
def monster_detail(request, pk):
    monster = get_object_or_404(Monster, pk=pk)
    observations = monster.observations.all()
    comments= monster.comments.all().order_by('-created_on')
    other_monsters= Monster.objects.exclude(pk=pk).order_by('name')

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.monster = monster
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added!')
            return redirect('articles:monster_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'articles/monster_detail.html', {'monster': monster, 'observations': observations, 'comments': comments, 'other_monsters': other_monsters, 'form': form})

#view for masterlist of observations by users
def observation_list(request):
    observations = Observation.objects.all()
    return render(request, 'articles/observation_list.html', {'observations': observations})

#view for each individual observation
def observation_detail(request, slug):
    observation = get_object_or_404(Observation, slug=slug)
    comments = observation.comments.all().order_by('-created_on')
    return render(request, 'articles/observation_detail.html', {'observation': observation, 'comments': comments})
