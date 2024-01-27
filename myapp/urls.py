from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('members/',views.members,name='members'),
    path('members/detail/<int:id>',views.detail,name='detail'),
    path('contact/',views.contact,name='contact'),
    path('hello/',views.hello,name='hello'),
    path('add_newmember/',views.add_newmember,name='add_newmember'),
    path('members/detail/update/<int:id>',views.update,name='update'),
    path('members/detail/delete/<int:id>',views.delete,name="delete"),
   
]