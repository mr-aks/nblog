from django.db import models
from django.db.models.base import Model, ModelState
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

class Blog(models.Model):
    user_id = models.ForeignKey(User,on_delete=CASCADE)
    tittle = models.CharField(max_length=50)
    Img = models.ImageField(upload_to='media/', blank=True, null=True)
    dsc = models.CharField(max_length=1500)
    pdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle