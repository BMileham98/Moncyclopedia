from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Monster(models.Model):
    """
    Model represents each monster to be listed and discussed
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    founder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='monsters')
    category = models.CharField(max_length=50)
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
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE, related_name='observations')
    title= models.CharField(max_length=200)
    observer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='observations')
    observation_date = models.DateField()
    location= models.CharField(max_length=255)
    observed_behaviour= models.TextField()
    danger_rating= models.CharField(max_length=50)
    additional_notes = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Observation of {self.monster.name} by {self.observer.username}"

class Comment(models.Model):
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.observation.title}"