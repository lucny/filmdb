# Z vestavěného modulu django.contrib importuje aplikaci admin
from django.contrib import admin
# Z vestavěného modulu django.urls importuje funkce path a include
from django.urls import path, include
# Z vestavěného modulu django.views.generic importuje třídu RedirectView
from django.views.generic import RedirectView
# Z vestavěného modulu django.conf.urls.static importuje funkci static
from django.conf.urls.static import static
# Ze stejné složky importuje modul settings
from . import settings

# Seznam (list) namapovaných cest - URL adres
urlpatterns = [
    # Zpřístupňuje adresy, které jsou součástí vestavěné administrační aplikace (v souboru urls.py)
    path('admin/', admin.site.urls),
    # Zpřístupňuje adresy, které jsou namapovány v naší aplikaci movies (v souboru urls.py)
    path('movies/', include('movies.urls')),
    # Domovská stránka je přesměrována na úvodní stránku aplikace movies
    path('', RedirectView.as_view(url='movies/')),
]

# Do seznamu urlpatterns přidává cestu k statickým souborům podle nastavení konstant v settings.py
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Do seznamu urlpatterns přidává cestu k uploadovaným souborům podle nastavení konstant v settings.py
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
