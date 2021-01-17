from django.contrib import admin
from .models import User
from .models import Auction_listing,bid,comments,watchlistt,maintainbid

# Register your models here.
admin.site.register(User)
admin.site.register(Auction_listing)
admin.site.register(bid)
admin.site.register(comments)
admin.site.register(watchlistt)
admin.site.register(maintainbid)
