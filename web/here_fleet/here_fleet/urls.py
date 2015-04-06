from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'here_fleet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'fleet.views.home', name='home'),
    url(r'^getVehiclePositions/',
        'fleet.views.get_vehicle_positions',
        name='get_vehicle_positions'),
    url(r'^getVehicleRoutes/([\d]+)/([\d]{4}-[\d]{2}-[\d]{2})/([\d]{4}-[\d]{2}-[\d]{2})',
        'fleet.views.get_vehicle_routes',
        name='get_vehicle_routes'),
]