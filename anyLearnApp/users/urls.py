from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users.forms import LoginForm

urlpatterns = [
     path('register/', views.RegisterView.as_view(), name='users-register'),
     path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
                                            authentication_form=LoginForm), name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
