from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.user_login,name='login'),
    path('register',views.register,name='register'),
    path('details/<int:id>',views.details,name='details'),
    path('post',views.user_post,name='post'),
    path('logout',views.user_logout,name='logout'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search/<int:id>',views.search,name='search'),
    path('changepassword',views.changepassword,name='changepassword'),





]
