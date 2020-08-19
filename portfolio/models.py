import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.translation import gettext as _

class MyUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username

class Person(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    display_picture = models.ImageField(default='default.png', upload_to='display_pictures') 

    def __str__(self):
        return f'{self.user.username} \'s info'
    
class Occupation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete = models.CASCADE)
    occupation = models.CharField(max_length = 100)


    def __str__(self):
        return f'{self.user.username} \'s occupation'

class Skills(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    skills = models.CharField(max_length = 100, blank=True)
    

    def __str__(self):
        return f'{self.occupation} \'s skillset'


class WorkExp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    company = models.CharField(max_length = 200, blank=True)
    YEAR_CHOICES = []
    for r in range(1980, (datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    started = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.now().year)
    left = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.now().year)
    position = models.CharField(max_length = 200, blank=True)


    def __str__(self):
        return f'{self.user.username} \'s work experiences'

class AcadExp(models.Model):  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    education = models.CharField(max_length = 30, blank=True)

    def __str__(self):
        return f'{self.user.username} \'s academic experiences'


class Contact(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE, blank=True)
    cell = models.CharField(max_length = 31)
    twitter = models.CharField(max_length = 100, blank=True)
    instagram = models.CharField(max_length = 100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return f'{self.user.username} \'s contact information'
