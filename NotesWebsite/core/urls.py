from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    # URL pattern for user login page

    path('', views.index, name='home'),
    # URL pattern for the home page (index) where user's notes are displayed

    path('logout/', views.logout, name='logout'),
    # URL pattern for user logout functionality

    path('signup/', views.signup, name='signup'),
    # URL pattern for user signup page

    path('makenote/', views.make_note, name='makenote'),
    # URL pattern for creating a new note

    path('notes/<str:pk>', views.note, name='note'),
    # URL pattern for viewing and updating a specific note

    path('delnote/<str:pk>', views.delnote, name='deletenote'),
    # URL pattern for deleting a specific note
]
