from django.urls import path
from BlogApp.views import blog

urlpatterns = [
    path('', blog, name="Blog"),
]