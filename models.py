from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction_listing(models.Model):
    category =models.CharField(max_length=64,blank=True,null=True)
    product_name=models.CharField(max_length=53,blank=True,null=True)
    product_info=models.CharField(max_length=53,blank=True,null=True)
    base_bid=models.IntegerField(null=True)
    img=models.ImageField(null=True,blank=True)

class maintainbid(models.Model):
    listing_details=models.ForeignKey(Auction_listing, on_delete=models.CASCADE,related_name="listing_details",null=True)
    biding_user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="biding_user",null=True)
    bid_price=models.IntegerField(null=True)



class bid(models.Model):
    user_id=models.ForeignKey(Auction_listing, on_delete=models.CASCADE,related_name="key",null=True)
    biding_price = models.IntegerField(null=True)

class comments(models.Model):
    cmnt= models.ForeignKey(Auction_listing,on_delete=models.CASCADE,related_name="cmnt",null=True)
    comment= models.CharField(max_length=200,blank=True,null=True)

class watchlistt(models.Model):
    u = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user",null=True)
    w_listing = models.ForeignKey(Auction_listing,on_delete=models.CASCADE,related_name="w_listing",null=True)
