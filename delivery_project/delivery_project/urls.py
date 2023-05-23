"""
URL configuration for delivery_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

# from api_restful.api.router import router_posts
# from rest_framework import routers
# from api_restful.api.views import EnvioViewSet
from api_restful.api.views import (
    EnvioListCreateView,
    EnvioRetrieveUpdateDeleteView,
    EstadoEnvioListCreateView,
    EstadoEnvioRetrieveUpdateDeleteView,
    SucursalListCreateView,
    SucursalRetrieveUpdateDeleteView
)


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router_posts.urls)),
    # path('', include(router.urls)),
    path('envios/', EnvioListCreateView.as_view(), name='envio-list-create'),
    path('envios/<int:pk>/', EnvioRetrieveUpdateDeleteView.as_view(), name='envio-retrieve-update-delete'),
    path('estados/', EstadoEnvioListCreateView.as_view(), name='estado-envio-list-create'),
    path('estados/<int:pk>/', EstadoEnvioRetrieveUpdateDeleteView.as_view(), name='estado-envio-retrieve-update-delete'),
    path('sucursales/', SucursalListCreateView.as_view(), name='sucursal-list-create'),
    path('sucursales/<int:pk>/', SucursalRetrieveUpdateDeleteView.as_view(), name='sucursal-Obtiene-Actualiza-Elimina'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]







