from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('signup',views.admin_signup,name='admin_signup'),
    path('login',views.admin_login,name='admin_login'),
    path('logout',views.admin_logout,name='admin_logout'),
    path('addpost',views.add_book,name='addpost'),
    path('updatepost/<int:id>',views.update_book,name='updatepost'),
    path('delete/<int:id>',views.delete_book,name='deletepost'),


]