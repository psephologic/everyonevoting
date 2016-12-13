from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view),
    url(r'^email/$', views.email_test),
    url(r'^login/$', views.login),
    url(r'^logout/$', auth_views.logout),
    #url(r'^account/', include('accounts.urls')),
    # url(r'^organizations/$', views.organizations),
    # url(r'^([A-Za-z-]*)', views.organization_lookup),
    # url(r'^([A-Za-z-]*)/locations/', include('locations.urls')),
    # url(r'^([A-Za-z-]*)/voters/', include('voters.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
