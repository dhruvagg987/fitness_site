from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userprofile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)

    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    calories = models.FloatField()

    def __str__(self):
        return self.user.username

    def wt(self):
        return self.weight/10

    def bmi(self):
        w = self.weight
        h=(self.height/100)**2
        return float("%0.2f" % (w/h))   