from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Tweet(models.Model):
    nickname = models.CharField(max_length=50,validators=[MinLengthValidator(1),MaxLengthValidator(50)])
    message = models.CharField(max_length=150,validators=[MinLengthValidator(1),MaxLengthValidator(150)])

    def __str__(self):
        return f"Tweet Nick: {self.nickname}, Message: {self.message}"
    

