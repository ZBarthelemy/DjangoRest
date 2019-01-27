from django.conf.urls import include
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Dummy API')

urlpatterns = [
    path('', include('products.urls')),
    path('swagger/', schema_view)
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]