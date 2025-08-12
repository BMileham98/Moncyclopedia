from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Monster(models.Model):
    """
    Model represents each monster to be listed and discussed
    """
    CATEGORY_CHOICES = [
        ('Chaos', 'Chaos'),
        ('Holy', 'Holy'),
        ('Marine', 'Marine'),
        ('Nature', 'Nature'),
        ('Aeries', 'Aeries'),
        ('Pyro', 'Pyro'),
        ('Twilight', 'Twilight'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    etymology = models.CharField(max_length=500)
    founder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='monsters')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    observed_size= models.TextField()
    description = models.TextField()
    observed_diet = models.TextField()
    habitat = models.TextField()
    signature_skill = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']


    def __str__(self):
        return self.name

class Observation(models.Model):

    DANGER_CHOICES = [
        (1, '1 - Harmless'),
        (2, '2 - Low Risk'),
        (3, '3 - Moderate'),
        (4, '4 - High Risk'),
        (5, '5 - Extremely Dangerous'),
    ]

    monster = models.ForeignKey(Monster, on_delete=models.CASCADE, related_name='observations')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    observer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='observations')
    observation_date = models.DateField()
    location = models.CharField(max_length=255)
    observed_behaviour = models.TextField()
    danger_rating = models.IntegerField(choices=DANGER_CHOICES)
    expanded_danger_rating = models.TextField()
    additional_notes = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Observation of {self.monster.name} by {self.observer.username}"
      
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1
            while Observation.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

class Comment(models.Model):
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        if self.observation:
            return f"Comment by {self.user.username} on {self.observation.title}"
        elif self.monster:
            return f"Comment by {self.user.username} on {self.monster.name}"
        return f"Comment by {self.user.username}"