from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Auction_listing,bid,comments,watchlistt,maintainbid

from .models import User


def index(request):
    data = Auction_listing.objects.all()
    return render(request, "auctions/index.html",{
    "data":data,
    })

def indexdetail(request,id):
    d = Auction_listing.objects.filter(id=id)
    return render(request,"auctions/indexdetail.html",{
    "d":d,
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

def create_listing(request):
    return render(request,"auctions/create_listing.html")


def save(request):
    if request.method == "POST":
        user_id=request.POST.get('Post_id')
        product_name=request.POST.get('product_name')
        category=request.POST.get('category')
        base_bid=request.POST.get('base_bid')
        product_info=request.POST.get('product_info')
        img=request.FILES.get('img')
        a = Auction_listing(category=category,product_name=product_name,base_bid=base_bid,product_info=product_info,img=img)
        a.save()

        return HttpResponseRedirect(reverse("index"))

def place_bid(request, id):
    if request.method =="POST":
        id = Auction_listing.objects.get(id=id)
        b_user = User.objects.get(id=request.user.id)
        a = maintainbid(biding_user=b_user,)

        old_bid=request.POST.get('old_bid')
        place_bid=request.POST.get('new_bid')
        if int(id.base_bid)>int(place_bid):
            return HttpResponse("Smaller Value")
        else:
            data2=Auction_listing.objects.filter(base_bid=old_bid).update(base_bid=place_bid)
            b=bid(biding_price=place_bid)
            b.save()
            return HttpResponseRedirect(reverse("index"))

def comment(request,id):
    return render(request,"auctions/comment.html", {
    "id":id
    })

def show_comments(request,id):
    getactions = Auction_listing.objects.get(id=id)
    cmnts=comments.objects.filter(cmnt = getactions)
    return render(request,"auctions/comment.html",{
    "cmnts":cmnts,
    "id":id
    })


def post_comment(request,id):
    if request.method =="POST":
        try:
            get = Auction_listing.objects.get(id=id)
        except Auction_listing.DoesNotExist:
            return HttpResponse("error")
        cmnt=request.POST.get('comment')
        c=comments(cmnt=get,comment=cmnt)
        c.save()
        return HttpResponse("posted")

def watchlist(request,id):
    got =Auction_listing.objects.get(id=id)
    try:
        a=watchlistt.objects.get(u=request.user,w_listing=got)
    except watchlistt.DoesNotExist:
        s=watchlistt(u=request.user , w_listing=got)
        s.save()
    a=watchlistt.objects.filter(u=request.user)

    return render(request,"auctions/watchlist.html",{
    "a":a
    })



def show_watchlist(request):
    return HttpResponseRedirect(reverse("watchlist",args=[27]))


def Category(request):
    cat=Auction_listing.objects.values('category')
    return render(request,"auctions/Category.html",{
    "cat":cat
      })

def cat_open(request,category):
    at=Auction_listing.objects.all().filter(category=category)
    return render(request,"auctions/Category.html",{
    "at":at
    })
