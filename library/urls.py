from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# Adding a permanent redirect for the root URL
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

# Enabling the serving of static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Django site authentication urls (for login, logut, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
