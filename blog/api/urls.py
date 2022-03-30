from django.urls import path
from blog.api import views

urlpatterns = [
    path('', views.BlogListCreateApi),
    path('<str:slug>/', views.BlogRetrieveDeleteApi),
]