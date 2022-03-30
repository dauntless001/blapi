from django.urls import path, include

urlpatterns = [
    path('blogs/', include('blog.api.urls')),
]
