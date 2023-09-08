from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    #nickname = models.CharField(max_length=50,validators=[MinLengthValidator(1),MaxLengthValidator(50)])
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=150,validators=[MinLengthValidator(1),MaxLengthValidator(150)])

    def __str__(self):
        return f"Tweet User: {self.username}, Message: {self.message}"
    

