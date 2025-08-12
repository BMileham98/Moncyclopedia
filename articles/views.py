from django.shortcuts import render, get_object_or_404, redirect # throw an error for user if request isn't valid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .models import Monster, Observation
from .forms import CommentForm, ObservationForm
from datetime import date

# Create your views here.

# home page function to allow featured monster
def index(request):
    monsters = Monster.objects.all()
    if monsters:
        today = date.today()
        # determining featured monster by element per weekday
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
        today_element = element_schedule[weekday]
        today_weekday = weekday_names[weekday]
        # sort monsters by element/category
        element_monsters = monsters.filter(category=today_element)
        if element_monsters:
            monster_index = today.toordinal() % element_monsters.count()
            featured_monster = element_monsters[monster_index]
            featured_element = today_element
        else: # if no monsters of this element, cycle through monsters
            monster_index = today.toordinal() % monsters.count()
            featured_monster = monsters[monster_index]
            featured_element = None
    else: # if no monsters are recalled, both are set to None
        featured_monster = None
        featured_element = None
    return render(request, 'index.html', {
        'featured_monster': featured_monster,
        'featured_element': featured_element,
        'day_name': today_weekday,
    })


# view for masterlist of monsters catalogued
def monster_list(request):
    monsters = Monster.objects.all().order_by('name')
    return render(request, 'articles/monster_list.html', {'monsters': monsters})

# view for each individual monster with list of related observations
def monster_detail(request, pk):
    monster = get_object_or_404(Monster, pk=pk)
    observations = monster.observations.all()
    comments = monster.comments.all().order_by('-created_on')
    other_monsters = Monster.objects.exclude(pk=pk).order_by('name')

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

# view for masterlist of observations by users
def observation_list(request):
    monsters_with_observations = Monster.objects.filter(observations__isnull=False).distinct().order_by('name')
    return render(request, 'articles/observation_list.html', {'monsters_with_observations': monsters_with_observations})

# view for each individual observation
def observation_detail(request, slug):
    observation = get_object_or_404(Observation, slug=slug)
    comments = observation.comments.all().order_by('-created_on')
    all_observations = Observation.objects.all().order_by('monster__name', 'observation_date')

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.observation = observation
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added!')
            return redirect('articles:observation_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'articles/observation_detail.html', {'observation': observation, 'comments': comments, 'all_observations': all_observations, 'form': form, })

@login_required
def create_observation(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST, request.FILES)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.observer = request.user

            if not observation.slug:
                from django.utils.text import slugify
                observation.slug = slugify(observation.title)
                
            observation.save()
            messages.success(request, 'Observation created successfully!')
            return redirect('articles:observation_detail', slug=observation.slug)
    else:
        form = ObservationForm()
    return render(request, 'articles/create_observation.html', {'form': form})

@login_required
def edit_observation(request, slug):
    observation= get_object_or_404(Observation, slug=slug)
    
    if observation.observer != request.user:
        return redirect('articles:observation_detail', slug=slug)

    if request.method == 'POST':
        form = ObservationForm(request.POST, request.FILES, instance=observation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Observation updated!')
            return redirect('articles:observation_detail', slug=slug)
    else:
        form = ObservationForm(instance=observation)
        
    return render(request, 'articles/edit_observation.html', {'form': form, 'observation': observation,})

@login_required
def delete_observation(request, slug):
    observation = get_object_or_404(Observation, slug=slug)
    
    if observation.observer != request.user:
        return redirect('articles:observation_detail', slug=slug)
    
    if request.method == 'POST':
        observation.delete()
        messages.success(request, 'Observation deleted successfully!')
        return redirect('articles:observation_list')
    
    return render(request, 'articles/delete_observation.html', {'observation': observation})