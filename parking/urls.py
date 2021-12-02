
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from parqueadero import views


schema_view = get_schema_view(
   openapi.Info(
      title="Documentación del Microservicio parqueadero",
      default_version='v 0.1',
      description="Documentación donde se describe el microservicio para la creación, consulta, eliminación y actualización de parqueaderos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="veroca989@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path("parking/create/", views.ParkingCreateView.as_view()),
    #path("parking/list/", views.ParkingListView.as_view()),
    path("parking/<int:pk>/", views.ParkingDetailView.as_view()), 
    path("parking/update/<int:pk>/", views.ParkingUpdateView.as_view()), 
    path("parking/delete/<int:pk>/", views.ParkingDeleteView.as_view()),
    
    
    
]
