from django.urls import path
from BlogApp.views import blog, categoria

urlpatterns = [
    path('', blog, name="Blog"),
    path('categoria/<categoria_id>/', categoria, name="Categoria"),
]