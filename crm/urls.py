from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'clients', views.СlientViewSet, basename='clients')
router.register(r'employee', views.EmployeeViewSet, basename='employee')
router.register(r'application', views.ApplicationViewSet, basename='application')



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    

]