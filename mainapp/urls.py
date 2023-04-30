from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #password change
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    #user registration
    path('register/', views.register, name='register'),

    #boooking
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),

    #off-hour
    path('offhour', views.offhour, name='offhour'),
    path('off-hour-submit', views.offhourSubmit, name='offhourSubmit'),
]