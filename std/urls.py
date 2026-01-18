
from django.urls import path
from .views import home,add_std,delete_std,update_std,register,login_page,logout_page

urlpatterns = [
   
    path('',home, name="home_page"),
    path('add-std/',add_std,name="add_std"),
    path('delete-std/<int:roll>/',delete_std,name="delete_page"),
    path('update-std/<int:roll>/',update_std,name="update_page"),
    path('register/', register, name="register_page"),
    path('login_page',login_page,name="login_page"),
    path("logout/",logout_page,name="logout_page")
    
]
