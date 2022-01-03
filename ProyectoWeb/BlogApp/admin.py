from django.contrib import admin
from BlogApp.models import Post, Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=("nombre","created")


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=("titulo", "autor")


admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)
