from django.urls import path
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Path for login
    path(route='login', view=views.login_user, name='login'),
    
    # Path for logout
    path(route='logout', view=views.logout_request, name='logout'),
    
    # Path for registration
    path(route='register', view=views.registration, name='registration'),
]