from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("indexdetail/<int:id>", views.indexdetail, name="indexdetail"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing",views.create_listing,name="create_listing"),
    path("save",views.save,name="save"),
    path("place_bid/<int:id>",views.place_bid,name="place_bid"),
    path("comment/<int:id>",views.comment,name="comment"),
    path("show_comments/<int:id>",views.show_comments,name="show_comments"),
    path("post_comment/<int:id>",views.post_comment,name="post_comment"),
    path("watchlist/<int:id>",views.watchlist,name="watchlist"),
    path("show_watchlist",views.show_watchlist,name="show_watchlist"),
    path("Category",views.Category,name="Category"),
    path("cat_open/<str:category>",views.cat_open,name="cat_open")




]
