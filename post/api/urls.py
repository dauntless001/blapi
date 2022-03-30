from django.urls import path
from post.api import views

urlpatterns = [
    path('', views.PostListCreateApi),
    path('<str:slug>/', views.PostRetrieveDeleteApi),
]