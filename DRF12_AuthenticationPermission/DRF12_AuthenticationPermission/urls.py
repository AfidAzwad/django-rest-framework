from django.contrib import admin
from django.urls import path, include
from AuthenticationPermission import views
from rest_framework.routers import DefaultRouter

# Create Router Object
router = DefaultRouter()

# Register StudentModelViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
