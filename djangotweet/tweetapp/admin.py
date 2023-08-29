from django.contrib import admin
from . import models

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    #fields = ["nickname","message"]

    fieldsets = [
        ("Message Group",{"fields":["message"]}),
        ("Nickname Group",{"fields":["nickname"]})
    ]

admin.site.register(models.Tweet,TweetAdmin)