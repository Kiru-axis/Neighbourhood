from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone


# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    hood_logo = models.ImageField(upload_to='hoods/',default='hood.jpg')
    description = models.TextField()
    health_workers = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)
    
    # create neighbourhood
    def create_neighbourhood(self):
        self.save()

    # delet neighbouthood
    def delete_neighbourhood(self):
        self.delete()
        
    # update neighbourhood
    @classmethod
    def update_neighbourhood(cls, id, value):
        cls.objects.filter(id=id).update(neighbourhood=value)
    
    # search neighbourhood
    @classmethod
    def find_neighbourhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
