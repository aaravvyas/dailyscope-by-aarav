from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout-confirm/', views.logout_confirm_view, name='logout_confirm'),
    path('profile/', views.profile_view, name='profile'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),  
    path('feedback/', views.feedback_view, name='feedback'),
]
