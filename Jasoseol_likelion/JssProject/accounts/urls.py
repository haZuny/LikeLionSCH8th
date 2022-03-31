from django.urls import path
from .views import signup
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logiout/', LogoutView.as_view(), name='logout'),
]

