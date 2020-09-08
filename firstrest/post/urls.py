
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


# django rest framework -> router -> url

# router = DefaultRouter()
# router.register('post', views.PostViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDtail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)