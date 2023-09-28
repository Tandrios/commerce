from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction, Watchlist, category_choices
from .forms import AuctionForm


def index(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.filter(active="Y").all(),
    })

def listing(request, auctionid):
    auction = Auction.objects.get(pk=auctionid)
    if request.method =="POST":
            if request.user.is_authenticated:
                if "add" in request.POST:
                    Watchlist.objects.create(user=request.user, auction=auction)
                elif "remove" in request.POST:
                    Watchlist.objects.filter(user=request.user, auction=auction).delete()
                elif "active" in request.POST:
                    print("active")
                    if request.user == auction.user:
                        if auction.active == "Y":
                            auction.active = "N"
                            auction.save()
                        else:
                            auction.active = "Y"
                            auction.save()
            else:
                return render(request, "auctions/listing.html", {
                    "message": "Not logged in"
                })
            
            return HttpResponseRedirect(reverse("listing", args=(auctionid, )))
    else:
        category = ""
        watchlist = {}
        
        for choice in category_choices:
            if choice[0] == auction.category:
                category = choice[1]

        if request.user.is_authenticated:
            watchlist = Watchlist.objects.filter(auction=Auction.objects.get(pk=auctionid), user=request.user).all()
        
        return render(request, "auctions/listing.html", {
                "auction": auction,
                "category": category,
                "watchlist": watchlist,
        })

@login_required
def watchlist(request):
    watchlist = Watchlist.objects.filter(user=request.user).all()
    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist
    })

@login_required
def create(request):
    if request.method == "POST":
        form = AuctionForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()

            return render(request, "auctions/create.html", {
                'message': "Form is valid"
            })
        else:
            return render(request, "auctions/create.html", {
                'message': "Form is invalid"
            })

    else:
        form = AuctionForm()
        
        return render(request, "auctions/create.html", {
            'form': form,
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
