from django.shortcuts import render, redirect
from . import models, forms
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def listtweet(request):
    all_tweets_data = models.Tweet.objects.all()
    all_tweets_dictionary = {"Tweets":all_tweets_data}

    return render(request, "tweetapp/listtweet.html", context=all_tweets_dictionary)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        #nickname = request.POST["nickname"]
        message = request.POST["message"]

        tweet_obj = models.Tweet(username=request.user,message=message)
        tweet_obj.save()

        #models.Tweet.objects.create(nickname,message)

        return(redirect(reverse("tweetapp:listtweet")))
    else:
        return render(request, "tweetapp/addtweet.html")
    
def addtweet_byform(request):
    if request.POST:

        form = forms.AddTweetForm(request.POST)
        if form.is_valid():
            #nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]

            tweet_obj = models.Tweet(username=request.user,message=message)
            tweet_obj.save()

            return(redirect(reverse("tweetapp:listtweet")))
        else:
            print("Error in Form!")
            return render(request, "tweetapp/addtweetbyform.html", context={"form":form})

    else:
        form = forms.AddTweetForm()
        return render(request, "tweetapp/addtweetbyform.html", context={"form":form})
    
def addtweet_bymodelform(request):
    if request.POST:
        form = forms.AddTweetModelForm(request.POST)
        if form.is_valid():
            #nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]

            tweet_obj = models.Tweet(username=request.user,message=message)
            tweet_obj.save()

            return(redirect(reverse("tweetapp:listtweet")))
        else:
            print("Error in Form!")
            return render(request, "tweetapp/addtweetbymodelform.html", context={"form":form})

    else:
        form = forms.AddTweetModelForm()
        return render(request, "tweetapp/addtweetbymodelform.html", context={"form":form})
    
@login_required(login_url="/login")
def deletetweet(request,id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return(redirect(reverse("tweetapp:listtweet")))


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"