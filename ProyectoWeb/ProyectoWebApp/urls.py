"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from ProyectoWebApp.views import home, servicios, tienda, blog, contacto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="Home"),
    path('servicios', servicios, name="Servicios"),
    path('tienda', tienda, name="Tienda"),
    path('blog', blog, name="Blog"),
    path('contacto', contacto, name="Contacto"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)